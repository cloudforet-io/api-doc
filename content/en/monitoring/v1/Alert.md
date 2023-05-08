---
title: "Alert"
linkTitle: "Alert"
weight: 3
bookFlatSection: true
---
# [Alert](#Alert)
desc: An Alert, a set of Events, is the smallest unit to manage incidents.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Alert


**Alert Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Alert#create) | [CreateAlertRequest](Alert#createalertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**update**](./Alert#update) | [UpdateAlertRequest](Alert#updatealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**update_state**](./Alert#update_state) | [UpdateAlertStateRequest](Alert#updatealertstaterequest) | [AlertInfo](./Alert#alertinfo) |
| [**merge**](./Alert#merge) | [MergeAlertRequest](Alert#mergealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**snooze**](./Alert#snooze) | [SnoozeAlertRequest](Alert#snoozealertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**add_responder**](./Alert#add_responder) | [AlertResponderRequest](Alert#alertresponderrequest) | [AlertInfo](./Alert#alertinfo) |
| [**remove_responder**](./Alert#remove_responder) | [AlertResponderRequest](Alert#alertresponderrequest) | [AlertInfo](./Alert#alertinfo) |
| [**add_project_dependency**](./Alert#add_project_dependency) | [AlertProjectDependencyRequest](Alert#alertprojectdependencyrequest) | [AlertInfo](./Alert#alertinfo) |
| [**remove_project_dependency**](./Alert#remove_project_dependency) | [AlertProjectDependencyRequest](Alert#alertprojectdependencyrequest) | [AlertInfo](./Alert#alertinfo) |
| [**delete**](./Alert#delete) | [AlertRequest](Alert#alertrequest) | [Empty](./Alert#empty) |
| [**get**](./Alert#get) | [GetAlertRequest](Alert#getalertrequest) | [AlertInfo](./Alert#alertinfo) |
| [**list**](./Alert#list) | [AlertQuery](Alert#alertquery) | [AlertsInfo](./Alert#alertsinfo) |
| [**stat**](./Alert#stat) | [AlertStatQuery](Alert#alertstatquery) | [Struct](./Alert#struct) |



    
<br>

### create

> **POST** /monitoring/v1/alert/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/alert/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### update_state

> **POST** /monitoring/v1/alert/update-state
>




 {{< tabs " update_state " >}}




{{< /tabs >}}

    
<br>

### merge

> **POST** /monitoring/v1/alert/merge
>




 {{< tabs " merge " >}}




{{< /tabs >}}

    
<br>

### snooze

> **POST** /monitoring/v1/alert/snooze
>




 {{< tabs " snooze " >}}




{{< /tabs >}}

    
<br>

### add_responder

> **POST** /monitoring/v1/alert/add-responder
>




 {{< tabs " add_responder " >}}




{{< /tabs >}}

    
<br>

### remove_responder

> **POST** /monitoring/v1/alert/remove-responder
>




 {{< tabs " remove_responder " >}}




{{< /tabs >}}

    
<br>

### add_project_dependency

> **POST** /monitoring/v1/alert/add-project-dependency
>




 {{< tabs " add_project_dependency " >}}




{{< /tabs >}}

    
<br>

### remove_project_dependency

> **POST** /monitoring/v1/alert/remove-project-dependency
>




 {{< tabs " remove_project_dependency " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /monitoring/v1/alert/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/alert/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/alert/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/alert/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### AlertInfo
* **alert_number** (int32)  `Required` 

    
* **alert_id** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **state** (AlertState)  `Required` 

    
* **status_message** (string)  `Required` 

    
* **description** (string)  `Required` 

    
* **assignee** (string)  `Required` 

    
* **urgency** (AlertUrgency)  `Required` 

    
* **severity** (string)  `Required` 

    
* **rule** (string)  `Required` 

    
* **resource** (AlertResource)  `Required` 

    
* **provider** (string)  `Required` 

    
* **account** (string)  `Required` 

    
* **is_snoozed** (bool)  `Required` 

    
* **snoozed_end_time** (string)  `Required` 

    
* **escalation_step** (int32)  `Required` 

    
* **escalation_ttl** (int32)  `Required` 

    
* **responders** (AlertResponder)  `Required` 

    
* **project_dependencies** (string)  `Required` 

    
* **image_url** (string)  `Required` 

    
* **additional_info** (Struct)  `Required` 

    
* **triggered_by** (string)  `Required` 

    
* **webhook_id** (string)  `Required` 

    
* **escalation_policy_id** (string)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **acknowledged_at** (string)  `Required` 

    
* **resolved_at** (string)  `Required` 

    
* **escalated_at** (string)  `Required` 

    <br>

### AlertProjectDependencyRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **alert_number** (int32)  `Required` 

  *is_required: false*

    
* **alert_id** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (AlertState)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **severity** (string)  `Required` 

  *is_required: false*

    
* **is_snoozed** (string)  `Required` 

  *is_required: false*

    
* **resource_id** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **account** (string)  `Required` 

  *is_required: false*

    
* **triggered_by** (string)  `Required` 

  *is_required: false*

    
* **webhook_id** (string)  `Required` 

  *is_required: false*

    
* **escalation_policy_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertResource
* **resource_id** (string)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **name** (string)  `Required` 

    <br>

### AlertResponder
* **resource_type** (string)  `Required` 

    
* **resource_id** (string)  `Required` 

    <br>

### AlertResponderRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **resource_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### AlertsInfo
* **results** (AlertInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateAlertRequest
* **title** (string)  `Required` 

  *is_required: true*

    
* **description** (string)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MergeAlertRequest
* **alerts** (string)  `Required` 

  *is_required: true*

    
* **merge_to** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SnoozeAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **end_time** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateAlertRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **status_message** (string)  `Required` 

  *is_required: false*

    
* **description** (string)  `Required` 

  *is_required: false*

    
* **assignee** (string)  `Required` 

  *is_required: false*

    
* **urgency** (AlertUrgency)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **reset_status_message** (bool)  `Required` 

  *is_required: false*

    
* **reset_description** (bool)  `Required` 

  *is_required: false*

    
* **reset_assignee** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateAlertStateRequest
* **alert_id** (string)  `Required` 

  *is_required: true*

    
* **access_key** (string)  `Required` 

  *is_required: true*

    
* **state** (string)  `Required` 

  *is_required: false*

    <br>
