---
title: "CostReport"
linkTitle: "CostReport"
weight: 3
bookFlatSection: true
---
# [CostReport](#CostReport)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## CostReport





**CostReport Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CostReport#create) | [CreateCostReportRequest](CostReport#createcostreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**update**](./CostReport#update) | [UpdateCostReportRequest](CostReport#updatecostreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**enable**](./CostReport#enable) | [CostReportRequest](CostReport#costreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**disable**](./CostReport#disable) | [CostReportRequest](CostReport#costreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**delete**](./CostReport#delete) | [CostReportRequest](CostReport#costreportrequest) | [Empty](CostReport#empty) |
| [**send**](./CostReport#send) | [SendCostReportRequest](CostReport#sendcostreportrequest) | [Struct](CostReport#struct) |
| [**run**](./CostReport#run) | [RunCostReportRequest](CostReport#runcostreportrequest) | [Empty](CostReport#empty) |
| [**get**](./CostReport#get) | [CostReportRequest](CostReport#costreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**list**](./CostReport#list) | [CostReportAnalyzeQuery](CostReport#costreportanalyzequery) | [CostReportInfos](CostReport#costreportinfos) |
| [**stat**](./CostReport#stat) | [CostReportStatQuery](CostReport#costreportstatquery) | [CostReportInfos](CostReport#costreportinfos) |



    
<br>

### create





> **POST** /cost-analysis/v1/cost-report/create
>






    
<br>

### update





> **POST** /cost-analysis/v1/cost-report/update
>






    
<br>

### enable





> **POST** /cost-analysis/v1/cost-report/enable
>






    
<br>

### disable





> **POST** /cost-analysis/v1/cost-report/disable
>






    
<br>

### delete





> **POST** /cost-analysis/v1/cost-report/delete
>






    
<br>

### send





> **POST** /cost-analysis/v1/cost-report/send
>






    
<br>

### run





> **POST** /cost-analysis/v1/cost-report/run
>






    
<br>

### get





> **POST** /cost-analysis/v1/cost-report/get
>






    
<br>

### list





> **POST** /cost-analysis/v1/cost-report/list
>






    
<br>

### stat





> **POST** /cost-analysis/v1/cost-report/stat
>






    


<br>
<br>

## Message



### CostReportAnalyzeQuery
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **query** (Query)  

    
* **issue_day** (string)  

    
* **recipients** (string)  `Repeated`   

    <br>

### CostReportInfo
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **issue_day** (string)   `Required` 

    
* **is_last_day** (bool)   `Required` 

    
* **currency** (string)   `Required` 

    
* **recipients** (string)  `Repeated`    `Required` 

    
* **data_sources** (string)  `Repeated`    `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CostReportInfos
* **results** (CostReportInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    <br>

### CostReportStatQuery
* **query** (StatisticsQuery)  

    <br>

### CreateCostReportRequest
* **currency** (string)   `Required` 

    
* **recipients** (string)  `Repeated`    `Required` 

    
* **issue_day** (string)  

    
* **is_last_day** (bool)  

    
* **data_source_filter** (Struct)  

    <br>

### RunCostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **report_date** (string)  

  *The report date is the Cost Report generated.*

    <br>

### SendCostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **workspace_id** (string)  

  *The Workspace ID which is related to cost report.*

    <br>

### UpdateCostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **start** (string)  

    
* **end** (string)  

    
* **issue_day** (string)  

    
* **currency** (string)  

    
* **recipients** (string)  `Repeated`   

    
* **data_sources** (string)  `Repeated`   

    <br>
