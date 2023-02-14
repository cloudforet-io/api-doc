---
description: A CollectorRule is a cloud service resource filtering the raw data from the Collector. The Cloud Service resource is created after the raw data is filtered by the CollectorRule.
---
# Collector rule

>  **Package : spaceone.api.inventory.v1**

## CollectorRule

{% hint style="info" %}
**CollectorRule Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](collector-rule.md#create)|   [CreateCollectorRuleRequest](collector-rule.md#createcollectorrulerequest) |   [CollectorRuleInfo](collector-rule.md#collectorruleinfo) |
| [**update**](collector-rule.md#update)|   [UpdateCollectorRuleRequest](collector-rule.md#updatecollectorrulerequest) |   [CollectorRuleInfo](collector-rule.md#collectorruleinfo) |
| [**change_order**](collector-rule.md#change_order)|   [ChangeCollectorRuleOrderRequest](collector-rule.md#changecollectorruleorderrequest) |   [CollectorRuleInfo](collector-rule.md#collectorruleinfo) |
| [**delete**](collector-rule.md#delete)|   [CollectorRuleRequest](collector-rule.md#collectorrulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](collector-rule.md#get)|   [GetCollectorRuleRequest](collector-rule.md#getcollectorrulerequest) |   [CollectorRuleInfo](collector-rule.md#collectorruleinfo) |
| [**list**](collector-rule.md#list)|   [CollectorRuleQuery](collector-rule.md#collectorrulequery) |   [CollectorRulesInfo](collector-rule.md#collectorrulesinfo) |
| [**stat**](collector-rule.md#stat)|   [CollectorRuleStatQuery](collector-rule.md#collectorrulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /inventory/v1/collector-rule/create
>

> Creates a new CollectorRule. When creating the cloud service, this method can apply two types of conditions: mapping projects where the cloud service incurred to the Cloud Service, and mapping cloud service accounts to the Cloud Service. By adjusting the `condition_policy` parameter, the CollectorRule can be applied when all conditions are met, applied when any of the conditions are met, or always applied regardless of whether the conditions are met.

| Type | Message |
| :--- | :--- |
| Request | [CreateCollectorRuleRequest](collector-rule.md#createcollectorrulerequest) |
| Response |  [CollectorRuleInfo](collector-rule.md#collectorruleinfo)  |
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
    "collector_id": "collector-2e39891cbbb5"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/collector-rule/update
>

> Updates a specific CollectorRule. You can make changes in CollectorRule settings, including filtering conditions.

| Type | Message |
| :--- | :--- |
| Request | [UpdateCollectorRuleRequest](collector-rule.md#updatecollectorrulerequest) |
| Response |  [CollectorRuleInfo](collector-rule.md#collectorruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### change_order
> **POST** /inventory/v1/collector-rule/change-order
>

> Changes the priority order of the CollectorRules to apply. If there are multiple CollectorRules applied in a specific service account, the priority order of the resources is required. This method changes the priority order to apply CollectorRules.

| Type | Message |
| :--- | :--- |
| Request | [ChangeCollectorRuleOrderRequest](collector-rule.md#changecollectorruleorderrequest) |
| Response |  [CollectorRuleInfo](collector-rule.md#collectorruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_rule_id": "collector-rule-c8055231e212",
    "order": 2
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/collector-rule/delete
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorRuleRequest](collector-rule.md#collectorrulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **POST** /inventory/v1/collector-rule/get
>


| Type | Message |
| :--- | :--- |
| Request | [GetCollectorRuleRequest](collector-rule.md#getcollectorrulerequest) |
| Response |  [CollectorRuleInfo](collector-rule.md#collectorruleinfo)  |
 
 

 
### list
> **POST** /inventory/v1/collector-rules/list
>

> Gets a list of all CollectorRules. You can use a query to get a filtered list of CollectorRules.

| Type | Message |
| :--- | :--- |
| Request | [CollectorRuleQuery](collector-rule.md#collectorrulequery) |
| Response |  [CollectorRulesInfo](collector-rule.md#collectorrulesinfo)  |
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/collector-rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorRuleStatQuery](collector-rule.md#collectorrulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeCollectorRuleOrderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_rule_id |string|✔| |
| order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |

### CollectorRuleActions
| Field | Type |  Description |
| :--- | :--- | :--- |
| change_project |string | |
| match_project |[MatchRule](collector-rule.md#matchrule) | |
| match_service_account |[MatchRule](collector-rule.md#matchrule) | |
| add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### CollectorRuleCondition
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| value |string | |
| operator |string | |

### CollectorRuleInfo
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
      <td style="text-align:left; width:100px;">collector_rule_id</td>
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
      <td style="text-align:left"><a href="collector-rule.md#collectorrulecondition">list of CollectorRuleCondition</a></td>
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
      <td style="text-align:left"><a href="collector-rule.md#collectorruleactions">CollectorRuleActions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="collector-rule.md#collectorruleoptions">CollectorRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">rule_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">collector_id</td>
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



### CollectorRuleOptions
| Field | Type |  Description |
| :--- | :--- | :--- |
| stop_processing |bool | |

### CollectorRuleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| collector_rule_id |string|✘| |
| name |string|✘| |
| data_source_id |string|✘| |
| domain_id |string|✔| |

### CollectorRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_rule_id |string|✔| |
| domain_id |string|✔| |

### CollectorRuleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CollectorRulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CollectorRuleInfo](collector-rule.md#collectorruleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCollectorRuleRequest
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
      <td style="text-align:left"><a href="collector-rule.md#collectorrulecondition">list of CollectorRuleCondition</a></td>
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
      <td style="text-align:left"><a href="collector-rule.md#collectorruleactions">CollectorRuleActions</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="collector-rule.md#collectorruleoptions">CollectorRuleOptions</a></td>
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
      <td style="text-align:left; width:100px;">collector_id</td>
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



### GetCollectorRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_rule_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MatchRule
| Field | Type |  Description |
| :--- | :--- | :--- |
| source |string | |
| target |string | |

### UpdateCollectorRuleRequest
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
      <td style="text-align:left; width:100px;">collector_rule_id</td>
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
      <td style="text-align:left"><a href="collector-rule.md#collectorrulecondition">list of CollectorRuleCondition</a></td>
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
      <td style="text-align:left"><a href="collector-rule.md#collectorruleactions">CollectorRuleActions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="collector-rule.md#collectorruleoptions">CollectorRuleOptions</a></td>
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


