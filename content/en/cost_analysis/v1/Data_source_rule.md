---
title: "Data_source_rule"
linkTitle: "Data_source_rule"
weight: 3
bookFlatSection: true
---
# [Data_source_rule](#Data_source_rule)
desc: A DataSourceRule is a resource filtering the raw data from the DataSource. The Cost resource is created after the raw data is filtered by the DataSourceRule.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Data_source_rule


**DataSourceRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DataSourceRule#create) | [CreateDataSourceRuleRequest](DataSourceRule#createdatasourcerulerequest) | [DataSourceRuleInfo](./DataSourceRule#datasourceruleinfo) |
| [**update**](./DataSourceRule#update) | [UpdateDataSourceRuleRequest](DataSourceRule#updatedatasourcerulerequest) | [DataSourceRuleInfo](./DataSourceRule#datasourceruleinfo) |
| [**change_order**](./DataSourceRule#change_order) | [ChangeDataSourceRuleOrderRequest](DataSourceRule#changedatasourceruleorderrequest) | [DataSourceRuleInfo](./DataSourceRule#datasourceruleinfo) |
| [**delete**](./DataSourceRule#delete) | [DataSourceRuleRequest](DataSourceRule#datasourcerulerequest) | [Empty](./DataSourceRule#empty) |
| [**get**](./DataSourceRule#get) | [GetDataSourceRuleRequest](DataSourceRule#getdatasourcerulerequest) | [DataSourceRuleInfo](./DataSourceRule#datasourceruleinfo) |
| [**list**](./DataSourceRule#list) | [DataSourceRuleQuery](DataSourceRule#datasourcerulequery) | [DataSourceRulesInfo](./DataSourceRule#datasourcerulesinfo) |
| [**stat**](./DataSourceRule#stat) | [DataSourceRuleStatQuery](DataSourceRule#datasourcerulestatquery) | [Struct](./DataSourceRule#struct) |



    
<br>

### create

> **POST** /cost-analysis/v1/data-source-rule/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/data-source-rule/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### change_order

> **POST** /cost-analysis/v1/data-source-rule/change-order
>




 {{< tabs " change_order " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/data-source-rule/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/data-source-rule/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/data-source-rule/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/data-source-rule/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ChangeDataSourceRuleOrderRequest
* **data_source_rule_id** (string)  `Required` 

  *is_required: true*

    
* **order** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CreateDataSourceRuleRequest
* **name** (string)  `Required` 

  *is_required: false*

    
* **conditions** (DataSourceRuleCondition)  `Required` 

  *is_required: false*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: true*

    
* **actions** (DataSourceRuleActions)  `Required` 

  *is_required: true*

    
* **options** (DataSourceRuleOptions)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceRuleActions
* **change_project** (string)  `Required` 

    
* **match_project** (MatchRule)  `Required` 

    
* **match_service_account** (MatchRule)  `Required` 

    
* **add_additional_info** (Struct)  `Required` 

    <br>

### DataSourceRuleCondition
* **key** (string)  `Required` 

    
* **value** (string)  `Required` 

    
* **operator** (string)  `Required` 

    <br>

### DataSourceRuleInfo
* **data_source_rule_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **order** (int32)  `Required` 

    
* **conditions** (DataSourceRuleCondition)  `Required` 

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

    
* **actions** (DataSourceRuleActions)  `Required` 

    
* **options** (DataSourceRuleOptions)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **rule_type** (string)  `Required` 

    
* **data_source_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### DataSourceRuleOptions
* **stop_processing** (bool)  `Required` 

    <br>

### DataSourceRuleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **data_source_rule_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceRuleRequest
* **data_source_rule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceRuleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceRulesInfo
* **results** (DataSourceRuleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetDataSourceRuleRequest
* **data_source_rule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### MatchRule
* **source** (string)  `Required` 

    
* **target** (string)  `Required` 

    <br>

### UpdateDataSourceRuleRequest
* **data_source_rule_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **conditions** (DataSourceRuleCondition)  `Required` 

  *is_required: false*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: false*

    
* **actions** (DataSourceRuleActions)  `Required` 

  *is_required: false*

    
* **options** (DataSourceRuleOptions)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
