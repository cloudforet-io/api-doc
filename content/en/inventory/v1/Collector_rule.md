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

desc: Creates a new CollectorRule. When creating the cloud service, this method can apply two types of conditions: mapping projects where the cloud service incurred to the Cloud Service, and mapping cloud service accounts to the Cloud Service. By adjusting the `condition_policy` parameter, the CollectorRule can be applied when all conditions are met, applied when any of the conditions are met, or always applied regardless of whether the conditions are met.
request_example: >-
{
"name": "match_service_account_test",
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {"source": "account", "target": "data.project_id"}
},
"options": {"stop_processing": true},
"tags": {"b": "c", "a": "b"},
"collector_id": "collector-2e39891cbbb5"
}
response_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account_test",
"order": 2,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {
"a": "b",
"b": "c"
},
"collector_id": "collector-2e39891cbbb5",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-19T10:13:28.335Z"
}



> **POST** /inventory/v1/collector-rule/create
>






    
<br>

### update

desc: Updates a specific CollectorRule. You can make changes in CollectorRule settings, including filtering conditions.
request_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account_test",
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {"b": "c", "a": "b"}
}
response_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account_test",
"order": 2,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {
"a": "b",
"b": "c"
},
"collector_id": "collector-2e39891cbbb5",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-19T10:13:28.335Z"
}



> **POST** /inventory/v1/collector-rule/update
>






    
<br>

### change_order

desc: Changes the priority order of the CollectorRules to apply. If there are multiple CollectorRules applied in a specific service account, the priority order of the resources is required. This method changes the priority order to apply CollectorRules.
request_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"order": 2
}
response_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account_test",
"order": 2,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {
"a": "b",
"b": "c"
},
"collector_id": "collector-2e39891cbbb5",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-19T10:13:28.335Z"
}



> **POST** /inventory/v1/collector-rule/change-order
>






    
<br>

### delete

desc: Deletes a specific CollectorRule. You must specify the `collector_rule_id` of the CollectorRule to delete.
request_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
}



> **POST** /inventory/v1/collector-rule/delete
>






    
<br>

### get

desc: Gets a specific CollectorRule. Prints detailed information about the CollectorRule, including  `conditions_policy` and conditions applied to Collector.
request_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
}
response_example: >-
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account",
"order": 1,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {},
"collector_id": "collector-2e39891cbbb5",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-25T16:01:51.858Z"
}



> **POST** /inventory/v1/collector-rule/get
>






    
<br>

### list

desc: Gets a list of all CollectorRules. You can use a query to get a filtered list of CollectorRules.
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"collector_rule_id": "collector-rule-c8055231e212",
"name": "match_service_account",
"order": 1,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.project_id"
}
},
"options": {
"stop_processing": true
},
"tags": {},
"collector_id": "collector-2e39891cbbb5",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-05-25T16:01:51.858Z"
},
{
"collector_rule_id": "collector-rule-t3345231e167",
"name": "match_service_account",
"order": 1,
"conditions_policy": "ALWAYS",
"actions": {
"match_service_account": {
"source": "account",
"target": "data.account_id"
}
},
"options": {
"stop_processing": true
},
"tags": {},
"collector_id": "collector-7163022d49a1",
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-03T16:00:54.099Z"
}
],
"total_count": 2
}



> **POST** /inventory/v1/collector-rules/list
>






    
<br>

### stat





> **POST** /inventory/v1/collector-rules/stat
>






    


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
