---
description: An EscalationPolicy is a set of rules to deliver an alert to assigned members.
---
# Escalation policy

>  **Package : spaceone.api.monitoring.v1**

## EscalationPolicy

{% hint style="info" %}
**EscalationPolicy Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](escalation-policy.md#create)|   [CreateEscalationPolicyRequest](escalation-policy.md#createescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |
| [**update**](escalation-policy.md#update)|   [UpdateEscalationPolicyRequest](escalation-policy.md#updateescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |
| [**set_default**](escalation-policy.md#set_default)|   [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |
| [**delete**](escalation-policy.md#delete)|   [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](escalation-policy.md#get)|   [GetEscalationPolicyRequest](escalation-policy.md#getescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |
| [**list**](escalation-policy.md#list)|   [EscalationPolicyQuery](escalation-policy.md#escalationpolicyquery) |   [EscalationPoliciesInfo](escalation-policy.md#escalationpoliciesinfo) |
| [**stat**](escalation-policy.md#stat)|   [EscalationPolicyStatQuery](escalation-policy.md#escalationpolicystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/escalation-policies
>

> Creates a new EscalationPolicy. When creating an EscalationPolicy, if the project_id is assigned, the EscalationPolicy is applied to the Project with the same project_id. If an EscalationPolicy is set as a global policy, all Projects in the same domain can apply the policy.

| Type | Message |
| :--- | :--- |
| Request | [CreateEscalationPolicyRequest](escalation-policy.md#createescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "es-test",
    "rules": [
        {
            "notification_level": "LV1",
            "escalate_minutes": 30
        },
        {
            "notification_level": "LV2",
            "escalate_minutes": 30
        }
    ],
    "repeat_count": 2,
    "finish_condition": "ACKNOWLEDGED",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "escalation_policy_id": "ep-526e536fdca9",
    "name": "es-test",
    "rules": [
        {
            "notification_level": "LV1",
            "escalate_minutes": 30
        },
        {
            "notification_level": "LV2",
            "escalate_minutes": 30
        }
    ],
    "repeat_count": 2,
    "finish_condition": "ACKNOWLEDGED",
    "scope": "GLOBAL",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-21T09:22:45.340Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /monitoring/v1/escalation-policy/{escalation_policy_id}
>

> Updates a specific EscalationPolicy. You can make changes in EscalationPolicy settings, including the name, the escalation process, and the number of iterations.

| Type | Message |
| :--- | :--- |
| Request | [UpdateEscalationPolicyRequest](escalation-policy.md#updateescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "escalation_policy_id": "ep-526e536fdca9",
    "name": "es-test2",
    "rules": [
        {
            "notification_level": "LV1",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV2",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV3",
            "escalate_minutes": 15
        }
    ],
    "repeat_count": 1,
    "finish_condition": "RESOLVED",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "escalation_policy_id": "ep-526e536fdca9",
    "name": "es-test2",
    "rules": [
        {
            "notification_level": "LV1",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV2",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV3",
            "escalate_minutes": 15
        }
    ],
    "repeat_count": 1,
    "finish_condition": "RESOLVED",
    "scope": "GLOBAL",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-21T09:22:45.340Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### set_default
> **PUT** /monitoring/v1/escalation-policy/{escalation_policy_id}/set-default
>

> Sets a specific EscalationPolicy as default. Only policies configured as global can be set as default. When a Project is created, even if you did not configure any policy to the Project, the default policy set by this api method is applied.

| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "escalation_policy_id": "ep-526e536fdca9",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "escalation_policy_id": "ep-526e536fdca9",
    "name": "es-test2",
    "is_default": true,
    "rules": [
        {
            "notification_level": "LV1",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV2",
            "escalate_minutes": 15
        },
        {
            "notification_level": "LV3",
            "escalate_minutes": 15
        }
    ],
    "repeat_count": 1,
    "finish_condition": "RESOLVED",
    "scope": "GLOBAL",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-21T09:22:45.340Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /monitoring/v1/escalation-policy/{escalation_policy_id}
>

> Deletes a specific EscalationPolicy. Deletes the EscalationPolicy with the escalation_policy_id from the deletion request.

| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "escalation_policy_id": "ep-d75670166af4",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /monitoring/v1/escalation-policy/{escalation_policy_id}
>

> Gets a specific EscalationPolicy. Prints detailed information about the EscalationPolicy, including the name, rules, and termination conditions.

| Type | Message |
| :--- | :--- |
| Request | [GetEscalationPolicyRequest](escalation-policy.md#getescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "escalation_policy_id": "ep-d75670166af4",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "escalation_policy_id": "ep-d75670166af4",
    "name": "0525-ms-test-2",
    "rules": [
        {
            "notification_level": "LV2",
            "escalate_minutes": 30
        },
        {
            "notification_level": "LV2"
        }
    ],
    "finish_condition": "ACKNOWLEDGED",
    "scope": "GLOBAL",
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-05-25T09:31:38.573Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/escalation-policies
>
> **POST** /monitoring/v1/escalation-policies/search


> Gets a list of all EscalationPolicies. You can use a query to get a filtered list of EscalationPolicies.

| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyQuery](escalation-policy.md#escalationpolicyquery) |
| Response |  [EscalationPoliciesInfo](escalation-policy.md#escalationpoliciesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "escalation_policy_id": "ep-7c9745003372",
            "name": "0525-ms-test-1",
            "rules": [
                {
                    "notification_level": "LV1"
                }
            ],
            "finish_condition": "ACKNOWLEDGED",
            "scope": "GLOBAL",
            "tags": {},
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-05-25T09:31:15.150Z"
        },
        {
            "escalation_policy_id": "ep-d75670166af4",
            "name": "0525-ms-test-2",
            "rules": [
                {
                    "notification_level": "LV2",
                    "escalate_minutes": 30
                },
                {
                    "notification_level": "LV2"
                }
            ],
            "finish_condition": "ACKNOWLEDGED",
            "scope": "GLOBAL",
            "tags": {},
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-05-25T09:31:38.573Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/escalation-policies/stat
>


| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyStatQuery](escalation-policy.md#escalationpolicystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateEscalationPolicyRequest
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
      <td style="text-align:left; width:100px;">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
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



### EscalationPoliciesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### EscalationPolicyInfo
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
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_default</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
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



### EscalationPolicyQuery
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
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
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
      <td style="text-align:left; width:100px;">is_default</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
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



### EscalationPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| escalation_policy_id |string|✔| |
| domain_id |string|✔| |

### EscalationPolicyRule
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
      <td style="text-align:left; width:100px;">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalate_minutes</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EscalationPolicyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### GetEscalationPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| escalation_policy_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateEscalationPolicyRequest
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
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
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
      <td style="text-align:left; width:100px;">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
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


