---
title: "Job_task"
linkTitle: "Job_task"
weight: 3
bookFlatSection: true
---
# [Job_task](#Job_task)
desc: A JobTask is a task unit subdividing a Job. The division criteria are specified in each DataSource plugin.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Job_task


**JobTask Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get**](./JobTask#get) | [GetJobTaskRequest](JobTask#getjobtaskrequest) | [JobTaskInfo](./JobTask#jobtaskinfo) |
| [**list**](./JobTask#list) | [JobTaskQuery](JobTask#jobtaskquery) | [JobTasksInfo](./JobTask#jobtasksinfo) |
| [**stat**](./JobTask#stat) | [JobTaskStatQuery](JobTask#jobtaskstatquery) | [Struct](./JobTask#struct) |



    
<br>

### get

> **POST** /cost-analysis/v1/job-task/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/job-task/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/job-task/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### GetJobTaskRequest
* **job_task_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### JobTaskInfo
* **job_task_id** (string)  `Required` 

    
* **status** (Status)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **created_count** (int32)  `Required` 

    
* **error_code** (string)  `Required` 

    
* **error_message** (string)  `Required` 

    
* **job_id** (string)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **started_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **finished_at** (string)  `Required` 

    <br>

### JobTaskQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **job_task_id** (string)  `Required` 

  *is_required: false*

    
* **status** (Status)  `Required` 

  *is_required: false*

    
* **job_id** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobTaskStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobTasksInfo
* **results** (JobTaskInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
