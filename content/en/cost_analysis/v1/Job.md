---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)
desc: A Job is an act of collecting external cost data through plugins. The data to collect is defined in a plugin.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Job


**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**cancel**](./Job#cancel) | [JobRequest](Job#jobrequest) | [JobInfo](./Job#jobinfo) |
| [**get**](./Job#get) | [GetJobRequest](Job#getjobrequest) | [JobInfo](./Job#jobinfo) |
| [**list**](./Job#list) | [JobQuery](Job#jobquery) | [JobsInfo](./Job#jobsinfo) |
| [**stat**](./Job#stat) | [JobStatQuery](Job#jobstatquery) | [Struct](./Job#struct) |



    
<br>

### cancel

> **POST** /cost-analysis/v1/job/cancel
>




 {{< tabs " cancel " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/job/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/job/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/job/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ChangedInfo
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **filter** (Struct)  `Required` 

    <br>

### GetJobRequest
* **job_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### JobInfo
* **job_id** (string)  `Required` 

    
* **status** (Status)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **error_code** (string)  `Required` 

    
* **error_message** (string)  `Required` 

    
* **total_tasks** (int32)  `Required` 

    
* **remained_tasks** (int32)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **finished_at** (string)  `Required` 

    
* **changed** (ChangedInfo)  `Required` 

    <br>

### JobQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **job_id** (string)  `Required` 

  *is_required: false*

    
* **status** (Status)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobRequest
* **job_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### JobsInfo
* **results** (JobInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
