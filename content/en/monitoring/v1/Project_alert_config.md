---
title: "Project_alert_config"
linkTitle: "Project_alert_config"
weight: 3
bookFlatSection: true
---
# [Project_alert_config](#Project_alert_config)
desc: A ProjectAlertConfig is a resource to set the alert policies for a Project.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Project_alert_config





**ProjectAlertConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./ProjectAlertConfig#create) | [CreateProjectAlertConfigRequest](ProjectAlertConfig#createprojectalertconfigrequest) | [ProjectAlertConfigInfo](./ProjectAlertConfig#projectalertconfiginfo) |
| [**update**](./ProjectAlertConfig#update) | [UpdateProjectAlertConfigRequest](ProjectAlertConfig#updateprojectalertconfigrequest) | [ProjectAlertConfigInfo](./ProjectAlertConfig#projectalertconfiginfo) |
| [**delete**](./ProjectAlertConfig#delete) | [ProjectAlertConfigRequest](ProjectAlertConfig#projectalertconfigrequest) | [Empty](./ProjectAlertConfig#empty) |
| [**get**](./ProjectAlertConfig#get) | [GetProjectAlertConfigRequest](ProjectAlertConfig#getprojectalertconfigrequest) | [ProjectAlertConfigInfo](./ProjectAlertConfig#projectalertconfiginfo) |
| [**list**](./ProjectAlertConfig#list) | [ProjectAlertConfigQuery](ProjectAlertConfig#projectalertconfigquery) | [ProjectAlertConfigsInfo](./ProjectAlertConfig#projectalertconfigsinfo) |
| [**stat**](./ProjectAlertConfig#stat) | [ProjectAlertConfigStatQuery](ProjectAlertConfig#projectalertconfigstatquery) | [Struct](./ProjectAlertConfig#struct) |



    
<br>

### create

desc: Creates a new ProjectAlertConfig in a specific Project. When creating a ProjectAlertConfig, validation of the Project is preceded. After the validation is done, ProjectAlertConfig enables EscalationPolicy to be set in the Project, or enables `enum` type `recovery_mode` and `notification_urgency` to be set through the `options` parameter.  The parameter `recovery_mode` is for changing the state of the Alert to `resolved` if the external monitoring solution sends the resolved Alert. The parameter `notification_urgency` is used to choose whether you will get all Alerts or only urgent ones.
request_example: >-
{
"project_id": "project-dee2a81d4859",
"escalation_policy_id": "ep-b441abe04ca9",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "AUTO"
},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"project_id": "project-dee2a81d4859",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "AUTO"
},
"escalation_policy_info": {
"escalation_policy_id": "ep-b441abe04ca9",
"name": "Global New Policy"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-27T05:12:22.998Z"
}



> **POST** /monitoring/v1/project-alert-config/create
>






    
<br>

### update

desc: Updates a specific ProjectAlertConfig. You can make changes in ProjectAlertConfig settings, including the EscalationPolicy to apply. You can also change `notification_urgency` and `recovery_mode` by modifying the `options` parameter.
request_example: >-
{
"project_id": "project-dee2a81d4859",
"escalation_policy_id": "ep-4ee42a9b2d96",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "MANUAL"
},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"project_id": "project-dee2a81d4859",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "MANUAL"
},
"escalation_policy_info": {
"escalation_policy_id": "ep-4ee42a9b2d96",
"name": "HAHA",
"is_default": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-27T05:15:02.697Z"
}



> **POST** /monitoring/v1/project-alert-config/update
>






    
<br>

### delete

desc: Deletes a specific ProjectAlertConfig. Deletes alert configuration data in a Project.
request_example: >-
{
"project_id": "project-dee2a81d4859",
"domain_id": "domain-58010aa2e451"
}



> **POST** /monitoring/v1/project-alert-config/delete
>






    
<br>

### get

desc: Gets a specific ProjectAlertConfig. Prints detailed information about the ProjectAlertConfig, including EscalationPolicy, recovery mode, and notification urgency.
request_example: >-
{
"project_id": "project-430bf6ab1e6d",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"project_id": "project-430bf6ab1e6d",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "AUTO"
},
"escalation_policy_info": {
"escalation_policy_id": "ep-4ee42a9b2d96",
"name": "HAHA",
"is_default": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-03T08:17:11.715Z"
}



> **POST** /monitoring/v1/project-alert-config/get
>






    
<br>

### list

desc: Gets a list of all ProjectAlertConfigs from all projects configured in the same domain. You can use a query to get a filtered list of ProjectAlertConfigs.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"results": [
{
"project_id": "project-18655561c535",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "MANUAL"
},
"escalation_policy_info": {
"escalation_policy_id": "ep-4ee42a9b2d96",
"name": "HAHA",
"is_default": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-17T02:09:19.839Z"
},
{
"project_id": "project-9074eea97d7e",
"options": {
"notification_urgency": "ALL",
"recovery_mode": "MANUAL"
},
"escalation_policy_info": {
"escalation_policy_id": "ep-b441abe04ca9",
"name": "Global New Policy"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2021-06-24T02:50:50.535Z"
}
],
"total_count": 2
}



> **POST** /monitoring/v1/project-alert-config/list
>






    
<br>

### stat





> **POST** /monitoring/v1/project-alert-config/stat
>






    


<br>
<br>

## Message



### AlertOptions
* **notification_urgency** (UrgencyOption)  `Required` 

    
* **recovery_mode** (RecoveryOption)  `Required` 

    <br>

### CreateProjectAlertConfigRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **options** (AlertOptions)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetProjectAlertConfigRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### ProjectAlertConfigInfo
* **project_id** (string)  `Required` 

    
* **options** (AlertOptions)  `Required` 

    
* **escalation_policy_info** (EscalationPolicyInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### ProjectAlertConfigQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectAlertConfigRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectAlertConfigStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ProjectAlertConfigsInfo
* **results** (ProjectAlertConfigInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateProjectAlertConfigRequest
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **options** (AlertOptions)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
