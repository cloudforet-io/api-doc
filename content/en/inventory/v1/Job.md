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

desc: Deletes a specific Job. You must specify the `job_id` of the Job to delete.
request_example: >-
{
"job_id": "job-123456789012",
"domain_id": "domain-123456789012"
}



> **POST** /inventory/v1/job/delete
>






    
<br>

### get

desc: Gets a specific Job. Prints detailed information about the Job, including its state, total tasks, and collector info.
request_example: >-
{
"job_id": "job-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"job_id": "job-123456789012",
"status": "ERROR",
"filter": {},
"total_tasks": 2,
"collector_info": {
"collector_id": "collector-123456789012",
"name": "Jenkins Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-jenkins-inven-collector",
"version": "0.1.1"
},
"provider": "jenkins",
"capability": {},
"is_public": true
},
"domain_id": "domain-123456789012",
"created_at": "2022-01-01T10:00:01.389Z",
"updated_at": "2022-01-01T10:00:01.389Z",
"finished_at": "2022-01-01T10:02:11.270Z"
}



> **POST** /inventory/v1/job/get
>






    
<br>

### list

desc: Gets a list of all Jobs. You can use a query to get a filtered list of Jobs.
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"job_id": "job-3b124006c2d2",
"status": "SUCCESS",
"filter": {},
"total_tasks": 2,
"collector_info": {
"collector_id": "collector-accd02663b3d",
"name": "openstack-collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-openstack-inven-collector",
"version": "0.4.2.20220616.134758"
},
"provider": "openstack",
"capability": {
"supported_schema": [
"openstack_credentials"
]
},
"is_public": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:01.225Z",
"updated_at": "2022-06-17T08:00:01.225Z",
"finished_at": "2022-06-17T08:00:15.197Z"
},
{
"job_id": "job-587a3d3b4db3",
"status": "SUCCESS",
"filter": {},
"total_tasks": 3,
"collector_info": {
"collector_id": "collector-2c0847644f39",
"name": "AWS stat-kwon Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142"
},
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:00.407Z",
"updated_at": "2022-06-17T08:00:00.407Z",
"finished_at": "2022-06-17T08:07:32.023Z"
}
],
"total_count": 2
}



> **POST** /inventory/v1/job/list
>






    
<br>

### stat





> **POST** /inventory/v1/job/stat
>






    


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
