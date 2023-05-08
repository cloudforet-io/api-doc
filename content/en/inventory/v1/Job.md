---
title: "Job"
linkTitle: "Job"
weight: 3
bookFlatSection: true
---
# [Job](#Job)
desc: A Job is an act of collecting external cloud resources through plugins.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Job


**Job Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**delete**](./Job#delete) | [JobRequest](Job#jobrequest) | [Empty](./Job#empty) |
| [**get**](./Job#get) | [GetJobRequest](Job#getjobrequest) | [JobInfo](./Job#jobinfo) |
| [**list**](./Job#list) | [JobsQuery](Job#jobsquery) | [JobsInfo](./Job#jobsinfo) |
| [**stat**](./Job#stat) | [JobStatQuery](Job#jobstatquery) | [Struct](./Job#struct) |



    
<br>

### delete

> **POST** /inventory/v1/job/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/job/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/job/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/job/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### GetJobRequest
* **job_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

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

### JobsQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **job_id** (string)  `Required` 

  *is_required: false*

    
* **status** (JobStatus)  `Required` 

  *is_required: false*

    
* **collector_id** (string)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
