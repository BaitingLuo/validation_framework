# verification Workflow Description 
The following description will tell the user how to prepare and execute the workflow for a succesfull
repreat of the original experiment.

## Environment
For the execution environment, you are going to need a linux based machine with [cwltool](https://github.com/common-workflow-language/cwltool)
installed on it. Additionally, you will also need [docker](https://docs.docker.com/engine/install/) installed to be able to run
the containerized computing elements.

## Description

### verification


### Required inputs
 - Parameter_config : 
 - X_train : 
 - y_test : 
 - y_train : 
 - X_test : 
 - Model_script : 


### Generated outputs
 - LIME_interpretation : 
 - SHapley_ouput : 
 - bootstrapping_output : 
 - ROC_plot : 


## Execution
To run the workflow, you need to give the following command:
```
cwltool --no-match-user --no-read-only --tmpdir $PWD --preserve-environment LEAP_CLI_DIR validation_pipeline.cwl.json --X_train X_train.csv --y_train y_train.csv --X_test X_test.csv --y_test y_test.csv --Model_script model_script.py --Parameter_config model_config.yaml 
```
Or
```
cwltool --no-match-user --no-read-only --tmpdir $PWD --preserve-environment LEAP_CLI_DIR validation_pipeline.cwl.json --X_train X_train.csv --y_train y_train.csv --X_test X_test.csv --y_test y_test.csv --Model_script sklearn.pkl --Parameter_config model_config.yaml 
```
The parameters in model_config.yaml file needs to be changed accordingly.
