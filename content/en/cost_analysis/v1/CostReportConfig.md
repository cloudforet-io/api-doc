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





> **POST** /cost-analysis/v1/cost-report/create
>






    
<br>

### update





> **POST** /cost-analysis/v1/cost-report/update
>






    
<br>

### update_recipients





> **POST** /cost-analysis/v1/cost-report/update-recipients
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



### CostReportConfigInfo
* **cost_report_config_id** (string)   `Required` 

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

### CostReportConfigQuery
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **query** (Query)  

    
* **state** (State)  

    <br>

### CostReportConfigRequest
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    <br>

### CostReportConfigStatQuery
* **query** (StatisticsQuery)  

    <br>

### CostReportConfigsInfo
* **results** (CostReportConfigInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCostReportConfigRequest
* **currency** (string)   `Required` 

    
* **recipients** (Struct)   `Required` 

    
* **issue_day** (int32)  

    
* **is_last_day** (bool)  

    
* **data_source_filter** (Struct)  

    <br>

### SendCostReportConfigRequest
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **workspace_id** (string)  

  *The Workspace ID which is related to cost report.*

    <br>

### UpdateCostReportConfigRecipientsRequest
* **cost_report_config_id** (string)   `Required` 

    
* **recipients** (Struct)  

    <br>

### UpdateCostReportConfigRequest
* **cost_report_config_id** (string)   `Required` 

  *The ID of cost report in the Protocol.*

    
* **issue_day** (string)  

    
* **is_last_day** (bool)  

    
* **currency** (string)  

    
* **data_source_filter** (Struct)  

    <br>
