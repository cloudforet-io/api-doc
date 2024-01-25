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
* **query** (TimeSeriesAnalyzeQuery)  

    
* **product** (string)  

    
* **provider** (string)  

    
* **workspace_id** (string)  

    
* **cost_report_config_id** (string)  

    
* **data_source_id** (string)  

    <br>

### CostReportDataInfo
* **cost_report_data_id** (string)   `Required` 

    
* **cost** (Struct)   `Required` 

    
* **cost_report_name** (string)   `Required` 

    
* **issue_date** (string)   `Required` 

    
* **report_year** (string)   `Required` 

    
* **report_month** (string)   `Required` 

    
* **is_confirmed** (bool)   `Required` 

    
* **provider** (string)   `Required` 

    
* **product** (string)   `Required` 

    
* **service_account_name** (string)   `Required` 

    
* **data_source_name** (string)   `Required` 

    
* **project_name** (string)   `Required` 

    
* **workspace_name** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **cost_report_config_id** (string)   `Required` 

    
* **cost_report_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **service_account_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### CostReportDataQuery
* **query** (Query)  

    
* **cost_report_data_id** (string)  

    
* **product** (string)  

    
* **provider** (string)  

    
* **is_confirmed** (bool)  

    
* **workspace_id** (string)  

    
* **cost_report_config_id** (string)  

    
* **cost_report_id** (string)  

    
* **data_source_id** (string)  

    <br>

### CostReportDataStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **cost_report_id** (string)  

    <br>

### CostReportsDataInfo
* **results** (CostReportDataInfo)  `Repeated`    `Required` 

    
* **total_count** (string)   `Required` 

    <br>

### StatInfo
* **results** (string)  `Repeated`    `Required` 

    <br>
