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
| [**send**](./CostReport#send) | [CostReportRequest](CostReport#costreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**get_url**](./CostReport#get_url) | [GetUrlCostReportRequest](CostReport#geturlcostreportrequest) | [Struct](CostReport#struct) |
| [**get**](./CostReport#get) | [CostReportRequest](CostReport#costreportrequest) | [CostReportInfo](CostReport#costreportinfo) |
| [**list**](./CostReport#list) | [CostReportQuery](CostReport#costreportquery) | [CostReportsInfo](CostReport#costreportsinfo) |
| [**stat**](./CostReport#stat) | [CostReportStatQuery](CostReport#costreportstatquery) | [Struct](CostReport#struct) |



    
<br>

### send





> **POST** /cost-analysis/v1/cost-report/send
>






    
<br>

### get_url





> **POST** /cost-analysis/v1/cost-report/get-url
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



### CostReportInfo
* **cost_report_id** (string)   `Required` 

    
* **cost** (Struct)   `Required` 

    
* **status** (Status)   `Required` 

    
* **cost_report_number** (string)   `Required` 

    
* **currency** (string)   `Required` 

    
* **issue_date** (string)   `Required` 

    
* **report_year** (string)   `Required` 

  *YYYY*

    
* **report_month** (string)   `Required` 

  *YYYY-mm*

    
* **workspace_name** (string)   `Required` 

    
* **cost_report_config_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### CostReportQuery
* **cost_report_id** (string)   `Required` 

    
* **query** (Query)  

    
* **workspace_name** (string)  

    
* **issue_date** (string)  

    <br>

### CostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    <br>

### CostReportStatQuery
* **query** (StatisticsQuery)  

    <br>

### CostReportsInfo
* **results** (CostReportInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetUrlCostReportRequest
* **cost_report_id** (string)   `Required` 

  *The ID of cost report in the Protocol*

    <br>
