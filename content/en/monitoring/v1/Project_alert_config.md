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

> **POST** /monitoring/v1/project-alert-config/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/project-alert-config/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/project-alert-config/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/project-alert-config/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/project-alert-config/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/project-alert-config/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
