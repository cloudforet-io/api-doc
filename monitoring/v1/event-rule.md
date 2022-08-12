---
description: An EventRule is a rule to transform the request data when an Event is generated.
---
# Event rule

>  **Package : spaceone.api.monitoring.v1**

## EventRule

{% hint style="info" %}
**EventRule Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](event-rule.md#create)|   [CreateEventRuleRequest](event-rule.md#createeventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |
| [**update**](event-rule.md#update)|   [UpdateEventRuleRequest](event-rule.md#updateeventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |
| [**change_order**](event-rule.md#change_order)|   [ChangeEventRuleOrderRequest](event-rule.md#changeeventruleorderrequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |
| [**delete**](event-rule.md#delete)|   [EventRuleRequest](event-rule.md#eventrulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](event-rule.md#get)|   [GetEventRuleRequest](event-rule.md#geteventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |
| [**list**](event-rule.md#list)|   [EventRuleQuery](event-rule.md#eventrulequery) |   [EventRulesInfo](event-rule.md#eventrulesinfo) |
| [**stat**](event-rule.md#stat)|   [EventRuleStatQuery](event-rule.md#eventrulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/event-rules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateEventRuleRequest](event-rule.md#createeventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/event-rule/{event_rule_id}
>

> Changes a priority order between EventRules to apply. EventRules are filtered by the order configured.

| Type | Message |
| :--- | :--- |
| Request | [UpdateEventRuleRequest](event-rule.md#updateeventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "conditions": [
        {
            "key": "description",
            "value": "ELB",
            "operator": "contain"
        }
    ],
    "conditions_policy": "ALL",
    "actions": {
        "change_assignee": "user2@email.com",
        "change_urgency": "HIGH",
        "change_project": "project-123456789012",
        "add_additional_info": {
            "type": "personal rule"
        },
        "no_notification": true
    },
    "options": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "order": 2,
    "conditions": [
        {
            "key": "description",
            "value": "ELB",
            "operator": "contain"
        }
    ],
    "conditions_policy": "ALL",
    "actions": {
        "change_assignee": "user2@email.com",
        "change_urgency": "HIGH",
        "change_project": "project-123456789012",
        "add_additional_info": {
            "type": "personal rule"
        },
        "no_notification": true
    },
    "options": {},
    "scope": "PROJECT",
    "project_id": "project-123456789012",
    "tags": {},
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:02:31.517Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### change_order
> **PUT** /monitoring/v1/event-rule/{event_rule_id}/order
>

> Updates a specific EventRule. You can make changes in EventRule settings.

| Type | Message |
| :--- | :--- |
| Request | [ChangeEventRuleOrderRequest](event-rule.md#changeeventruleorderrequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "order": 2,
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "order": 2,
    "conditions": [
        {
            "key": "description",
            "value": "API",
            "operator": "contain"
        }
    ],
    "conditions_policy": "ALL",
    "actions": {
        "change_assignee": "user1@email.com",
        "change_urgency": "LOW",
        "change_project": "project-123456789012",
        "add_additional_info": {
            "type": "personal rule"
        },
        "no_notification": true
    },
    "options": {},
    "scope": "PROJECT",
    "project_id": "project-123456789012",
    "tags": {},
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-02T06:02:31.517Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /monitoring/v1/event-rule/{event_rule_id}
>

> Deletes a specific EventRule. You must assign an EventRule resource to delete by specifying `event_rule_id`.

| Type | Message |
| :--- | :--- |
| Request | [EventRuleRequest](event-rule.md#eventrulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /monitoring/v1/event-rule/{event_rule_id}
>

> Gets a specific EventRule. Prints detailed information about the EventRule.

| Type | Message |
| :--- | :--- |
| Request | [GetEventRuleRequest](event-rule.md#geteventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "event_rule_id": "er-123456789012",
    "order": 2,
    "conditions": [
        {
            "key": "title",
            "value": "ELB",
            "operator": "contain"
        }
    ],
    "conditions_policy": "ALL",
    "actions": {
        "change_assignee": "user1@email.com",
        "change_urgency": "LOW",
        "change_project": "project-123456789012",
        "add_additional_info": {},
        "no_notification": true
    },
    "options": {},
    "scope": "PROJECT",
    "project_id": "project-123456789012",
    "tags": {},
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T06:12:30.226Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/event-rules
>
> **POST** /monitoring/v1/event-rules/search


> Gets a list of all EventRules. You can use a query to get a filtered list of EventRules. For example, you can adjust the scope of the list to a certain Project or Domain.

| Type | Message |
| :--- | :--- |
| Request | [EventRuleQuery](event-rule.md#eventrulequery) |
| Response |  [EventRulesInfo](event-rule.md#eventrulesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "event_rule_id": "er-123456789012",
            "order": 1,
            "conditions": [
                {
                    "key": "title",
                    "value": "AWS",
                    "operator": "contain"
                }
            ],
            "conditions_policy": "ALL",
            "actions": {
                "change_assignee": "user2@email.com",
                "change_urgency": "HIGH",
                "add_additional_info": {},
                "no_notification": true
            },
            "options": {},
            "scope": "PROJECT",
            "project_id": "project-123456789012",
            "tags": {},
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T06:33:58.388Z"
        },
        {
            "event_rule_id": "er-123456789012",
            "order": 2,
            "conditions": [
                {
                    "key": "title",
                    "value": "ELB",
                    "operator": "contain"
                }
            ],
            "conditions_policy": "ALL",
            "actions": {
                "change_assignee": "user1@email.com",
                "change_urgency": "LOW",
                "change_project": "project-123456789012",
                "add_additional_info": {},
                "no_notification": true
            },
            "options": {},
            "scope": "PROJECT",
            "project_id": "project-123456789012",
            "tags": {},
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T06:12:30.226Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/event-rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [EventRuleStatQuery](event-rule.md#eventrulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeEventRuleOrderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| event_rule_id |string|✔| |
| order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
| domain_id |string|✔| |

### CreateEventRuleRequest
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
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">conditions</td>
      <td style="text-align:left"><a href="event-rule.md#eventrulecondition">list of EventRuleCondition</a></td>
<td style="text-align:center">✔</td>
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
      <td style="text-align:left"><a href="event-rule.md#eventruleactions">EventRuleActions</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="event-rule.md#eventruleoptions">EventRuleOptions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
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



### EventRuleActionResponder
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| resource_id |string | |

### EventRuleActions
| Field | Type |  Description |
| :--- | :--- | :--- |
| change_assignee |string | |
| change_urgency |string | |
| change_project |string | |
| add_project_dependency |list of string | |
| add_responder |[list of EventRuleActionResponder](event-rule.md#eventruleactionresponder) | |
| match_service_account |[MatchRule](event-rule.md#matchrule) | |
| add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| no_notification |bool | |

### EventRuleCondition
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| value |string | |
| operator |string | |

### EventRuleInfo
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
      <td style="text-align:left; width:100px;">event_rule_id</td>
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
      <td style="text-align:left"><a href="event-rule.md#eventrulecondition">list of EventRuleCondition</a></td>
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
      <td style="text-align:left"><a href="event-rule.md#eventruleactions">EventRuleActions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="event-rule.md#eventruleoptions">EventRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### EventRuleOptions
| Field | Type |  Description |
| :--- | :--- | :--- |
| stop_processing |bool | |

### EventRuleQuery
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
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">event_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
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



### EventRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| event_rule_id |string|✔| |
| domain_id |string|✔| |

### EventRuleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### EventRulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EventRuleInfo](event-rule.md#eventruleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetEventRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| event_rule_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MatchRule
| Field | Type |  Description |
| :--- | :--- | :--- |
| source |string | |
| target |string | |

### UpdateEventRuleRequest
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
      <td style="text-align:left; width:100px;">event_rule_id</td>
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
      <td style="text-align:left"><a href="event-rule.md#eventrulecondition">list of EventRuleCondition</a></td>
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
      <td style="text-align:left"><a href="event-rule.md#eventruleactions">EventRuleActions</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="event-rule.md#eventruleoptions">EventRuleOptions</a></td>
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


