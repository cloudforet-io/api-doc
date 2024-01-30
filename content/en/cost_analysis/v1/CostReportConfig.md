---
title: "CostReportConfig"
linkTitle: "CostReportConfig"
weight: 3
bookFlatSection: true
---
# [CostReportConfig](#CostReportConfig)



>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## CostReportConfig





**CostReportConfig Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CostReportConfig#create) | [CreateCostReportConfigRequest](CostReportConfig#createcostreportconfigrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**update**](./CostReportConfig#update) | [UpdateCostReportConfigRequest](CostReportConfig#updatecostreportconfigrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**update_recipients**](./CostReportConfig#update_recipients) | [UpdateCostReportConfigRecipientsRequest](CostReportConfig#updatecostreportconfigrecipientsrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**enable**](./CostReportConfig#enable) | [CostReportConfigRequest](CostReportConfig#costreportconfigrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**disable**](./CostReportConfig#disable) | [CostReportConfigRequest](CostReportConfig#costreportconfigrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**delete**](./CostReportConfig#delete) | [CostReportConfigRequest](CostReportConfig#costreportconfigrequest) | [Empty](CostReportConfig#empty) |
| [**run**](./CostReportConfig#run) | [CostReportConfigRequest](CostReportConfig#costreportconfigrequest) | [Empty](CostReportConfig#empty) |
| [**get**](./CostReportConfig#get) | [CostReportConfigRequest](CostReportConfig#costreportconfigrequest) | [CostReportConfigInfo](CostReportConfig#costreportconfiginfo) |
| [**list**](./CostReportConfig#list) | [CostReportConfigQuery](CostReportConfig#costreportconfigquery) | [CostReportConfigsInfo](CostReportConfig#costreportconfigsinfo) |
| [**stat**](./CostReportConfig#stat) | [CostReportConfigStatQuery](CostReportConfig#costreportconfigstatquery) | [CostReportConfigsInfo](CostReportConfig#costreportconfigsinfo) |



    
<br>

### create





> **POST** /cost-analysis/v1/cost-report-config/create
>






    
<br>

### update





> **POST** /cost-analysis/v1/cost-report-config/update
>






    
<br>

### update_recipients





> **POST** /cost-analysis/v1/cost-report-config/update-recipients
>






    
<br>

### enable





> **POST** /cost-analysis/v1/cost-report-config/enable
>






    
<br>

### disable





> **POST** /cost-analysis/v1/cost-report-config/disable
>






    
<br>

### delete





> **POST** /cost-analysis/v1/cost-report-config/delete
>






    
<br>

### run





> **POST** /cost-analysis/v1/cost-report-config/run
>






    
<br>

### get





> **POST** /cost-analysis/v1/cost-report-config/get
>






    
<br>

### list





> **POST** /cost-analysis/v1/cost-report-config/list
>






    
<br>

### stat





> **POST** /cost-analysis/v1/cost-report-config/stat
>






    


<br>
<br>

## Message



### CostReportConfigInfo
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **state** (State)   `Required` 

    
* **issue_day** (int32)   `Required` 

    
* **is_last_day** (bool)   `Required` 

    
* **currency** (string)   `Required` 

    
* **recipients** (Struct)   `Required` 

    
* **data_source_filter** (Struct)   `Required` 

    
* **language** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CostReportConfigQuery
* **query** (Query)  

    
* **cost_report_config_id** (string)  

  *The ID of cost report in the Protocol.*

    
* **state** (State)  

    <br>

### CostReportConfigRequest
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    <br>

### CostReportConfigStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### CostReportConfigsInfo
* **results** (CostReportConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCostReportConfigRequest
* **recipients** (Struct)   `Required` 

    
* **issue_day** (int32)  

    
* **is_last_day** (bool)  

    
* **currency** (string)  

    
* **data_source_filter** (Struct)  

    
* **language** (string)  

  *Default `en`*

    <br>

### UpdateCostReportConfigRecipientsRequest
* **cost_report_config_id** (string)   `Required` 

    
* **recipients** (Struct)  

    <br>

### UpdateCostReportConfigRequest
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **issue_day** (int32)  

    
* **is_last_day** (bool)  

    
* **currency** (string)  

    
* **data_source_filter** (Struct)  

    
* **language** (string)  

    <br>
