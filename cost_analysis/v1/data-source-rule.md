---
description: A DataSourceRule is a resource filtering the raw data from the DataSource. The Cost resource is created after the raw data is filtered by the DataSourceRule.
---
# Data source rule

>  **Package : spaceone.api.cost_analysis.v1**

## DataSourceRule

{% hint style="info" %}
**DataSourceRule Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](data-source-rule.md#create)|   [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |
| [**update**](data-source-rule.md#update)|   [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |
| [**change_order**](data-source-rule.md#change_order)|   [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |
| [**delete**](data-source-rule.md#delete)|   [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](data-source-rule.md#get)|   [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |   [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) |
| [**list**](data-source-rule.md#list)|   [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |   [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo) |
| [**stat**](data-source-rule.md#stat)|   [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/data_source_rules
>

> Creates a new DataSourceRule. When creating the resource, this method can apply two types of conditions: mapping projects where the cost incurred to the Cost, and mapping cloud service accounts to the Cost. By adjusting the `condition_policy` parameter, the DataSourceRule can be applied when all conditions are met, applied when any of the conditions are met, or always applied regardless of whether the conditions are met.

| Type | Message |
| :--- | :--- |
| Request | [CreateDataSourceRuleRequest](data-source-rule.md#createdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
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
    "tags": {
        "b": "c",
        "a": "b"
    },
    "data_source_id": "ds-c96609f5afeb"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>

> Updates a specific DataSourceRule. You can make changes in DataSourceRule settings, including filtering conditions. If the parameter `is_default` is `true`, only `Admin` type User can use this method.

| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRuleRequest](data-source-rule.md#updatedatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
    "tags": {
        "b": "c",
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### change_order
> **PUT** /cost-analysis/v1/data_source_rule/{data_source_rule_id}/order
>

> Changes the priority order of the DataSourceRules to apply. If there are multiple DataSourceRules applied in a specific service account, the priority order of the resources is requried. This method changes the priority order to apply DataSourceRules.

| Type | Message |
| :--- | :--- |
| Request | [ChangeDataSourceRuleOrderRequest](data-source-rule.md#changedatasourceruleorderrequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_rule_id": "rule-c8055231e212",
    "order": 2
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>

> Deletes a specific DataSourceRule. You must specify the `data_source_rule_id` of the DataSourceRule to delete. If the parameter `is_default` is `true`, only `Admin` type User can use this method.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleRequest](data-source-rule.md#datasourcerulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_rule_id": "rule-22fab02f6b51"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/data_source_rule/{data_source_rule_id}
>

> Gets a specific DataSourceRule. Prints detailed information about the DataSourceRule, including  `conditions_policy` and conditions applied to DataSources.

| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRuleRequest](data-source-rule.md#getdatasourcerulerequest) |
| Response |  [DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_rule_id": "rule-22fab02f6b51"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/data_source_rules
>
> **POST** /cost-analysis/v1/data_source_rules/search


> Gets a list of all DataSourceRules. You can use a query to get a filtered list of DataSourceRules.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleQuery](data-source-rule.md#datasourcerulequery) |
| Response |  [DataSourceRulesInfo](data-source-rule.md#datasourcerulesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/data_source_rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceRuleStatQuery](data-source-rule.md#datasourcerulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeDataSourceRuleOrderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✔| |
| order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |

### CreateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DataSourceRuleActions
| Field | Type |  Description |
| :--- | :--- | :--- |
| change_project |string | |
| match_project |[MatchRule](data-source-rule.md#matchrule) | |
| match_service_account |[MatchRule](data-source-rule.md#matchrule) | |
| add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### DataSourceRuleCondition
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| value |string | |
| operator |string | |

### DataSourceRuleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">order</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DataSourceRuleOptions
| Field | Type |  Description |
| :--- | :--- | :--- |
| stop_processing |bool | |

### DataSourceRuleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| data_source_rule_id |string|✘| |
| name |string|✘| |
| data_source_id |string|✘| |
| domain_id |string|✔| |

### DataSourceRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✔| |
| domain_id |string|✔| |

### DataSourceRuleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### DataSourceRulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DataSourceRuleInfo](data-source-rule.md#datasourceruleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDataSourceRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_rule_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MatchRule
| Field | Type |  Description |
| :--- | :--- | :--- |
| source |string | |
| target |string | |

### UpdateDataSourceRuleRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourcerulecondition">list of DataSourceRuleCondition</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions_policy</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>ANY</li>
          	<li>ALWAYS</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">actions</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleactions">DataSourceRuleActions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="data-source-rule.md#datasourceruleoptions">DataSourceRuleOptions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


