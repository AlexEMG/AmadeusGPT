import warnings

from amadeusgpt.config import Config
##########
# all these are providing the customized classes for the code execution
from amadeusgpt.programs.sandbox import Sandbox
##########
from amadeusgpt.utils import *

warnings.filterwarnings("ignore")
import os

from amadeusgpt.analysis_objects.llm import (CodeGenerationLLM, DiagnosisLLM,
                                             SelfDebugLLM, VisualLLM)
from amadeusgpt.integration_module_hub import IntegrationModuleHub

from amadeusgpt.analysis_objects.llm import (CodeGenerationLLM, DiagnosisLLM,
                                             SelfDebugLLM, VisualLLM)
from amadeusgpt.integration_module_hub import IntegrationModuleHub
from collections import defaultdict
import pickle 

from amadeusgpt.programs.task_program_registry import TaskProgramLibrary

class AMADEUS:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.code_generator_llm = CodeGenerationLLM(config.get("llm_info", {}))
        self.self_debug_llm = SelfDebugLLM(config.get("llm_info", {}))
        self.diagnosis_llm = DiagnosisLLM(config.get("llm_info", {}))
        self.visual_llm = VisualLLM(config.get("llm_info", {}))
        ### fields that decide the behavior of the application
        self.use_self_debug = True
        self.use_diagnosis = False
        self.use_behavior_modules_in_context = True
        self.smart_loading = False
        self.load_module_top_k = 3
        self.module_threshold = 0.3
        ### fields that serve as important storage
        # for long-term memory
        self.integration_module_hub = IntegrationModuleHub(config)
        #### sanbox that actually takes query and executes the code
        self.sandbox = Sandbox(config)
        ####

        ## register the llm to the sandbox
        self.sandbox.register_llm("code_generator", self.code_generator_llm)
        self.sandbox.register_llm("visual_llm", self.visual_llm)
        if self.use_self_debug:
            self.sandbox.register_llm("self_debug", self.self_debug_llm)
        if self.use_diagnosis:
            self.sandbox.register_llm("diagnosis", self.diagnosis_llm)

        # can only do this after the register process
        self.sandbox.configure_using_vlm()

    def match_integration_module(self, user_query: str):
        """
        Return a list of matched integration modules
        """
        sorted_query_results = self.integration_module_hub.match_module(user_query)
        if len(sorted_query_results) == 0:
            return None
        modules = []
        for i in range(min(self.load_module_top_k, len(sorted_query_results))):
            query_result = sorted_query_results[i]
            query_module = query_result[0]
            query_score = query_result[1][0][0]
            if query_score > self.module_threshold:
                modules.append(query_module)

                # parse the query result by loading active loading
        return modules  

    def step(self, user_query):
        integration_module_names = self.match_integration_module(user_query)
        self.sandbox.update_matched_integration_modules(integration_module_names)
        result = self.sandbox.llm_step(user_query)
        return result

    def get_analysis(self):
        """
        Every sandbox stores a unique "behavior analysis" instance in its namespace
        Therefore, get analysis gets the current sandbox's analysis.
        """
        analysis = self.sandbox.exec_namespace["behavior_analysis"]
        return analysis

    def run_task_program(self, config: Config, task_program_name: str):
        """
        Execute the task program on the currently holding sandbox
        Parameters
        -----------
        config: a config specifies the movie file and the keypoint file to run task program
        task_program_name: the name of the task program to run

        """
        return self.sandbox.run_task_program(config, task_program_name)
    
    def save_results(self, out_folder: str| None = None):
        """
        Save the results of the qa message (since it has all the information needed)
        """
        if out_folder is None:
            result_folder = self.sandbox.result_folder
        else:
            result_folder = out_folder
        # make sure it exists
        os.makedirs(result_folder, exist_ok=True)
        results = self.sandbox.result_cache

        ret = defaultdict(dict)
        for query in results:
            for video_file_path in results[query]:
                ret[query][video_file_path] = results[query][video_file_path].get_serializable()

        # save results to a pickle file
        with open (os.path.join(result_folder, "results.pickle"), "wb") as f:
            pickle.dump(ret, f)

    def load_results(self, result_folder: str | None = None ):
        if result_folder is None:
            result_folder = self.sandbox.result_folder
        else:
            result_folder = result_folder
        
        with open (os.path.join(result_folder, "results.pickle"), "rb") as f:
            results = pickle.load(f)
        self.sandbox.result_cache = results

    def get_results(self):
        return self.sandbox.result_cache
    
    def get_task_programs(self):
        return TaskProgramLibrary.get_task_programs()

if __name__ == "__main__":
    from amadeusgpt.analysis_objects.llm import VisualLLM
    from amadeusgpt.config import Config
    config = Config("amadeusgpt/configs/EPM_template.yaml")
    amadeus = AMADEUS(config)   
