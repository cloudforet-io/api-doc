---
title: "DataSourceRule"
linkTitle: "DataSourceRule"
weight: 3
bookFlatSection: true
---
# [DataSourceRule](#DataSourceRule)
A DataSourceRule is a resource filtering the raw data from the DataSource. The Cost resource is created after the raw data is filtered by the DataSourceRule.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## DataSourceRule





**DataSourceRule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DataSourceRule#create) | [CreateDataSourceRuleRequest](DataSourceRule#createdatasourcerulerequest) | [DataSourceRuleInfo](DataSourceRule#datasourceruleinfo) |
| [**update**](./DataSourceRule#update) | [UpdateDataSourceRuleRequest](DataSourceRule#updatedatasourcerulerequest) | [DataSourceRuleInfo](DataSourceRule#datasourceruleinfo) |
| [**change_order**](./DataSourceRule#change_order) | [ChangeDataSourceRuleOrderRequest](DataSourceRule#changedatasourceruleorderrequest) | [DataSourceRuleInfo](DataSourceRule#datasourceruleinfo) |
| [**delete**](./DataSourceRule#delete) | [DataSourceRuleRequest](DataSourceRule#datasourcerulerequest) | [Empty](DataSourceRule#empty) |
| [**get**](./DataSourceRule#get) | [DataSourceRuleRequest](DataSourceRule#datasourcerulerequest) | [DataSourceRuleInfo](DataSourceRule#datasourceruleinfo) |
| [**list**](./DataSourceRule#list) | [DataSourceRuleQuery](DataSourceRule#datasourcerulequery) | [DataSourceRulesInfo](DataSourceRule#datasourcerulesinfo) |
| [**stat**](./DataSourceRule#stat) | [DataSourceRuleStatQuery](DataSourceRule#datasourcerulestatquery) | [Struct](DataSourceRule#struct) |



    
<br>

### create

Creates a new DataSourceRule. When creating the resource, this method can apply two types of conditions: mapping projects where the cost incurred to the Cost, and mapping cloud service accounts to the Cost. By adjusting the `condition_policy` parameter, the DataSourceRule can be applied when all conditions are met, applied when any of the conditions are met, or always applied regardless of whether the conditions are met.



> **POST** /cost-analysis/v1/data-source-rule/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateDataSourceRuleRequest](./DataSourceRule#createdatasourcerulerequest)

* **data_source_id** (string)   `Required` 


* **conditions_policy** (ConditionsPolicy)   `Required` 


* **actions** (DataSourceRuleActions)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **workspace_id** (string)   `Required` 


* **name** (string)  


* **conditions** (DataSourceRuleCondition)  `Repeated`   


* **options** (DataSourceRuleOptions)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "data_source_id": "ds-c96609f5afeb",
   "name": "match_service_account_test",
   "conditions_policy": "ALWAYS",
   "actions": {
       "match_service_account": {"source": "account", "target": "data.project_id"}
   },
   "options": {"stop_processing": true},
   "tags": {"b": "c", "a": "b"}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceRuleInfo](#DATASOURCERULEINFO)
* **data_source_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **rule_type** (RuleType)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (DataSourceRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (DataSourceRuleActions)   `Required` 

* **options** (DataSourceRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
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
   "data_source_id": "ds-c96609f5afeb",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T10:13:28.335Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific DataSourceRule. You can make changes in DataSourceRule settings, including filtering conditions. If the parameter `is_default` is `true`, only `Admin` type User can use this method.



> **POST** /cost-analysis/v1/data-source-rule/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateDataSourceRuleRequest](./DataSourceRule#updatedatasourcerulerequest)

* **data_source_rule_id** (string)   `Required` 


* **name** (string)  


* **conditions** (DataSourceRuleCondition)  `Repeated`   


* **conditions_policy** (ConditionsPolicy)  


* **actions** (DataSourceRuleActions)  


* **options** (DataSourceRuleOptions)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceRuleInfo](#DATASOURCERULEINFO)
* **data_source_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **rule_type** (RuleType)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (DataSourceRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (DataSourceRuleActions)   `Required` 

* **options** (DataSourceRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
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
   "data_source_id": "ds-c96609f5afeb",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T10:13:28.335Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### change_order

Changes the priority order of the DataSourceRules to apply. If there are multiple DataSourceRules applied in a specific service account, the priority order of the resources is requried. This method changes the priority order to apply DataSourceRules.



> **POST** /cost-analysis/v1/data-source-rule/change-order
>





 {{< tabs " change_order " >}}

 {{< tab "Request Example" >}}



[ChangeDataSourceRuleOrderRequest](./DataSourceRule#changedatasourceruleorderrequest)

* **data_source_rule_id** (string)   `Required` 


* **order** (int32)   `Required` 





{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
   "order": 2
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceRuleInfo](#DATASOURCERULEINFO)
* **data_source_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **rule_type** (RuleType)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (DataSourceRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (DataSourceRuleActions)   `Required` 

* **options** (DataSourceRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
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
   "data_source_id": "ds-c96609f5afeb",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T10:13:28.335Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific DataSourceRule. You must specify the `data_source_rule_id` of the DataSourceRule to delete. If the parameter `is_default` is `true`, only `Admin` type User can use this method.



> **POST** /cost-analysis/v1/data-source-rule/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[DataSourceRuleRequest](./DataSourceRule#datasourcerulerequest)

* **data_source_rule_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_rule_id": "rule-22fab02f6b51"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific DataSourceRule. Prints detailed information about the DataSourceRule, including  `conditions_policy` and conditions applied to DataSources.



> **POST** /cost-analysis/v1/data-source-rule/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[DataSourceRuleRequest](./DataSourceRule#datasourcerulerequest)

* **data_source_rule_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_rule_id": "rule-22fab02f6b51"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceRuleInfo](#DATASOURCERULEINFO)
* **data_source_rule_id** (string)   `Required` 

* **name** (string)   `Required` 

* **rule_type** (RuleType)   `Required` 

* **order** (int32)   `Required` 

* **conditions** (DataSourceRuleCondition)  `Repeated`   `Required` 

* **conditions_policy** (ConditionsPolicy)   `Required` 

* **actions** (DataSourceRuleActions)   `Required` 

* **options** (DataSourceRuleOptions)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **data_source_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
{
   "data_source_rule_id": "rule-c8055231e212",
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
   "data_source_id": "ds-c96609f5afeb",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T10:13:28.335Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all DataSourceRules. You can use a query to get a filtered list of DataSourceRules.



> **POST** /cost-analysis/v1/data-source-rule/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[DataSourceRuleQuery](./DataSourceRule#datasourcerulequery)

* **query** (Query)  


* **data_source_rule_id** (string)  


* **name** (string)  


* **rule_type** (RuleType)  


* **workspace_id** (string)  


* **data_source_id** (string)  





{{< highlight json >}}
{
 "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceRulesInfo](#DATASOURCERULESINFO)
* **results** (DataSourceRuleInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
       "results": [
           {
               "data_source_rule_id": "rule-22fab02f6b51",
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
               "data_source_id": "ds-c96609f5afeb",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-05-25T16:01:51.858Z"
           },
           {
               "data_source_rule_id": "rule-188d366e9817",
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
               "data_source_id": "ds-fcba92ca73b1",
               "domain_id": "domain-58010aa2e451",
               "created_at": "2022-06-03T16:00:54.099Z"
           }
       ],
       "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/data-source-rule/stat
>






    


<br>
<br>

## Message



### ChangeDataSourceRuleOrderRequest
* **data_source_rule_id** (string)   `Required` 

    
* **order** (int32)   `Required` 

    <br>

### CreateDataSourceRuleRequest
* **data_source_id** (string)   `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (DataSourceRuleActions)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (DataSourceRuleCondition)  `Repeated`   

    
* **options** (DataSourceRuleOptions)  

    
* **tags** (Struct)  

    <br>

### DataSourceRuleActions
* **change_project** (string)   `Required` 

    
* **match_project** (MatchRule)   `Required` 

    
* **match_service_account** (MatchRule)   `Required` 

    
* **add_additional_info** (Struct)   `Required` 

    <br>

### DataSourceRuleCondition
* **key** (string)   `Required` 

    
* **value** (string)   `Required` 

    
* **operator** (string)   `Required` 

    <br>

### DataSourceRuleInfo
* **data_source_rule_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **rule_type** (RuleType)   `Required` 

    
* **order** (int32)   `Required` 

    
* **conditions** (DataSourceRuleCondition)  `Repeated`    `Required` 

    
* **conditions_policy** (ConditionsPolicy)   `Required` 

    
* **actions** (DataSourceRuleActions)   `Required` 

    
* **options** (DataSourceRuleOptions)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **data_source_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### DataSourceRuleOptions
* **stop_processing** (bool)   `Required` 

    <br>

### DataSourceRuleQuery
* **query** (Query)  

    
* **data_source_rule_id** (string)  

    
* **name** (string)  

    
* **rule_type** (RuleType)  

    
* **workspace_id** (string)  

    
* **data_source_id** (string)  

    <br>

### DataSourceRuleRequest
* **data_source_rule_id** (string)   `Required` 

    <br>

### DataSourceRuleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### DataSourceRulesInfo
* **results** (DataSourceRuleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### MatchRule
* **source** (string)   `Required` 

    
* **target** (string)   `Required` 

    <br>

### UpdateDataSourceRuleRequest
* **data_source_rule_id** (string)   `Required` 

    
* **name** (string)  

    
* **conditions** (DataSourceRuleCondition)  `Repeated`   

    
* **conditions_policy** (ConditionsPolicy)  

    
* **actions** (DataSourceRuleActions)  

    
* **options** (DataSourceRuleOptions)  

    
* **tags** (Struct)  

    <br>
