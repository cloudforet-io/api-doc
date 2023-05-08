---
title: "Collector_rule"
linkTitle: "Collector_rule"
weight: 3
bookFlatSection: true
---
# [Collector_rule](#Collector_rule)
desc: A CollectorRule is a cloud service resource filtering the raw data from the Collector. The Cloud Service resource is created after the raw data is filtered by the CollectorRule.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Collector_rule


**CollectorRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CollectorRule#create) | [CreateCollectorRuleRequest](CollectorRule#createcollectorrulerequest) | [CollectorRuleInfo](./CollectorRule#collectorruleinfo) |
| [**update**](./CollectorRule#update) | [UpdateCollectorRuleRequest](CollectorRule#updatecollectorrulerequest) | [CollectorRuleInfo](./CollectorRule#collectorruleinfo) |
| [**change_order**](./CollectorRule#change_order) | [ChangeCollectorRuleOrderRequest](CollectorRule#changecollectorruleorderrequest) | [CollectorRuleInfo](./CollectorRule#collectorruleinfo) |
| [**delete**](./CollectorRule#delete) | [CollectorRuleRequest](CollectorRule#collectorrulerequest) | [Empty](./CollectorRule#empty) |
| [**get**](./CollectorRule#get) | [GetCollectorRuleRequest](CollectorRule#getcollectorrulerequest) | [CollectorRuleInfo](./CollectorRule#collectorruleinfo) |
| [**list**](./CollectorRule#list) | [CollectorRuleQuery](CollectorRule#collectorrulequery) | [CollectorRulesInfo](./CollectorRule#collectorrulesinfo) |
| [**stat**](./CollectorRule#stat) | [CollectorRuleStatQuery](CollectorRule#collectorrulestatquery) | [Struct](./CollectorRule#struct) |



    
<br>

### create

> **POST** /inventory/v1/collector-rule/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/collector-rule/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### change_order

> **POST** /inventory/v1/collector-rule/change-order
>




 {{< tabs " change_order " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/collector-rule/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/collector-rule/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/collector-rules/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/collector-rules/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ChangeCollectorRuleOrderRequest
* **collector_rule_id** (string)  `Required` 

  *is_required: true*

    
* **order** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorRuleActions
* **change_project** (string)  `Required` 

    
* **match_project** (MatchRule)  `Required` 

    
* **match_service_account** (MatchRule)  `Required` 

    
* **add_additional_info** (Struct)  `Required` 

    <br>

### CollectorRuleCondition
* **key** (string)  `Required` 

    
* **value** (string)  `Required` 

    
* **operator** (string)  `Required` 

    <br>

### CollectorRuleInfo
* **collector_rule_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **order** (int32)  `Required` 

    
* **conditions** (CollectorRuleCondition)  `Required` 

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

    
* **actions** (CollectorRuleActions)  `Required` 

    
* **options** (CollectorRuleOptions)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **rule_type** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### CollectorRuleOptions
* **stop_processing** (bool)  `Required` 

    <br>

### CollectorRuleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **collector_rule_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorRuleRequest
* **collector_rule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorRuleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorRulesInfo
* **results** (CollectorRuleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCollectorRuleRequest
* **name** (string)  `Required` 

  *is_required: false*

    
* **conditions** (CollectorRuleCondition)  `Required` 

  *is_required: false*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: true*

    
* **actions** (CollectorRuleActions)  `Required` 

  *is_required: true*

    
* **options** (CollectorRuleOptions)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetCollectorRuleRequest
* **collector_rule_id** (string)  `Required` 

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

### UpdateCollectorRuleRequest
* **collector_rule_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **conditions** (CollectorRuleCondition)  `Required` 

  *is_required: false*

    
* **conditions_policy** (ConditionsPolicy)  `Required` 

  *is_required: false*

    
* **actions** (CollectorRuleActions)  `Required` 

  *is_required: false*

    
* **options** (CollectorRuleOptions)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
