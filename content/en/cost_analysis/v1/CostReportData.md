---
title: "CostReportData"
linkTitle: "CostReportData"
weight: 3
bookFlatSection: true
---
# [CostReportData](#CostReportData)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## CostReportData





**CostReportData Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](./CostReportData#list) | [CostReportDataQuery](CostReportData#costreportdataquery) | [CostReportsDataInfo](CostReportData#costreportsdatainfo) |
| [**analyze**](./CostReportData#analyze) | [CostReportDataAnalyzeQuery](CostReportData#costreportdataanalyzequery) | [Struct](CostReportData#struct) |
| [**stat**](./CostReportData#stat) | [CostReportDataStatQuery](CostReportData#costreportdatastatquery) | [Struct](CostReportData#struct) |



    
<br>

### list





> **POST** /cost-analysis/v1/cost-report-data/list
>






    
<br>

### analyze





> **POST** /cost-analysis/v1/cost-report-data/analyze
>






    
<br>

### stat





> **POST** /cost-analysis/v1/cost-report-data/stat
>






    


<br>
<br>

## Message



### CostReportDataAnalyzeQuery
* **cost_report_id** (string)   `Required` 

    
* **query** (TimeSeriesAnalyzeQuery)  

    
* **product** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **data_source_id** (string)  

    <br>

### CostReportDataInfo
* **cost** (Struct)   `Required` 

    
* **cost_report_name** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **product** (string)   `Required` 

    
* **project_name** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **service_account_name** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **data_source_name** (string)   `Required` 

    
* **workspace_name** (string)   `Required` 

    
* **report_year** (string)   `Required` 

    
* **report_month** (string)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **icons** (Struct)   `Required` 

    
* **domain_config** (Struct)   `Required` 

    
* **cost_report_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CostReportDataQuery
* **query** (Query)  

    
* **cost_report_id** (string)  

    
* **product** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **data_source_id** (string)  

    <br>

### CostReportDataStatQuery
* **query** (StatisticsQuery)  

    
* **cost_report_id** (string)  

    <br>

### CostReportsDataInfo
* **results** (CostReportDataInfo)  `Repeated`    `Required` 

    
* **total_count** (string)   `Required` 

    <br>

### StatInfo
* **results** (string)  `Repeated`    `Required` 

    <br>
