---
description: A ProjectAlertConfig is a resource to set the alert policies for a Project.
---
# Project alert config

>  **Package : spaceone.api.monitoring.v1**

## ProjectAlertConfig

{% hint style="info" %}
**ProjectAlertConfig Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](project-alert-config.md#create)|   [CreateProjectAlertConfigRequest](project-alert-config.md#createprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |
| [**update**](project-alert-config.md#update)|   [UpdateProjectAlertConfigRequest](project-alert-config.md#updateprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |
| [**delete**](project-alert-config.md#delete)|   [ProjectAlertConfigRequest](project-alert-config.md#projectalertconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](project-alert-config.md#get)|   [GetProjectAlertConfigRequest](project-alert-config.md#getprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |
| [**list**](project-alert-config.md#list)|   [ProjectAlertConfigQuery](project-alert-config.md#projectalertconfigquery) |   [ProjectAlertConfigsInfo](project-alert-config.md#projectalertconfigsinfo) |
| [**stat**](project-alert-config.md#stat)|   [ProjectAlertConfigStatQuery](project-alert-config.md#projectalertconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/project-alert-config/create
>

> Creates a new ProjectAlertConfig in a specific Project. When creating a ProjectAlertConfig, validation of the Project is preceded. After the validation is done, ProjectAlertConfig enables EscalationPolicy to be set in the Project, or enables `enum` type `recovery_mode` and `notification_urgency` to be set through the `options` parameter.  The parameter `recovery_mode` is for changing the state of the Alert to `resolved` if the external monitoring solution sends the resolved Alert. The parameter `notification_urgency` is used to choose whether you will get all Alerts or only urgent ones.

| Type | Message |
| :--- | :--- |
| Request | [CreateProjectAlertConfigRequest](project-alert-config.md#createprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_id": "project-dee2a81d4859",
    "escalation_policy_id": "ep-b441abe04ca9",
    "options": {
        "notification_urgency": "ALL",
        "recovery_mode": "AUTO"
    },
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "project_id": "project-dee2a81d4859",
    "options": {
        "notification_urgency": "ALL",
        "recovery_mode": "AUTO"
    },
    "escalation_policy_info": {
        "escalation_policy_id": "ep-b441abe04ca9",
        "name": "Global New Policy"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-27T05:12:22.998Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /monitoring/v1/project-alert-config/update
>

> Updates a specific ProjectAlertConfig. You can make changes in ProjectAlertConfig settings, including the EscalationPolicy to apply. You can also change `notification_urgency` and `recovery_mode` by modifying the `options` parameter.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectAlertConfigRequest](project-alert-config.md#updateprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_id": "project-dee2a81d4859",
    "escalation_policy_id": "ep-4ee42a9b2d96",
    "options": {
        "notification_urgency": "ALL",
        "recovery_mode": "MANUAL"
    },
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "project_id": "project-dee2a81d4859",
    "options": {
        "notification_urgency": "ALL",
        "recovery_mode": "MANUAL"
    },
    "escalation_policy_info": {
        "escalation_policy_id": "ep-4ee42a9b2d96",
        "name": "HAHA",
        "is_default": true
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-27T05:15:02.697Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /monitoring/v1/project-alert-config/delete
>

> Deletes a specific ProjectAlertConfig. Deletes alert configuration data in a Project.

| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigRequest](project-alert-config.md#projectalertconfigrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_id": "project-dee2a81d4859",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /monitoring/v1/project-alert-config/get
>

> Gets a specific ProjectAlertConfig. Prints detailed information about the ProjectAlertConfig, including EscalationPolicy, recovery mode, and notification urgency.

| Type | Message |
| :--- | :--- |
| Request | [GetProjectAlertConfigRequest](project-alert-config.md#getprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "project_id": "project-430bf6ab1e6d",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "project_id": "project-430bf6ab1e6d",
    "options": {
        "notification_urgency": "ALL",
        "recovery_mode": "AUTO"
    },
    "escalation_policy_info": {
        "escalation_policy_id": "ep-4ee42a9b2d96",
        "name": "HAHA",
        "is_default": true
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-05-03T08:17:11.715Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /monitoring/v1/project-alert-config/list
>

> Gets a list of all ProjectAlertConfigs from all projects configured in the same domain. You can use a query to get a filtered list of ProjectAlertConfigs.

| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigQuery](project-alert-config.md#projectalertconfigquery) |
| Response |  [ProjectAlertConfigsInfo](project-alert-config.md#projectalertconfigsinfo)  |
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
            "project_id": "project-18655561c535",
            "options": {
                "notification_urgency": "ALL",
                "recovery_mode": "MANUAL"
            },
            "escalation_policy_info": {
                "escalation_policy_id": "ep-4ee42a9b2d96",
                "name": "HAHA",
                "is_default": true
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-05-17T02:09:19.839Z"
        },
        {
            "project_id": "project-9074eea97d7e",
            "options": {
                "notification_urgency": "ALL",
                "recovery_mode": "MANUAL"
            },
            "escalation_policy_info": {
                "escalation_policy_id": "ep-b441abe04ca9",
                "name": "Global New Policy"
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2021-06-24T02:50:50.535Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/project-alert-config/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigStatQuery](project-alert-config.md#projectalertconfigstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AlertOptions
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
      <td style="text-align:left; width:100px;">notification_urgency</td>
      <td style="text-align:left"><ul>
          	<li>URGENCY_NONE</li>
          	<li>ALL</li>
          	<li>HIGH_ONLY</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">recovery_mode</td>
      <td style="text-align:left"><ul>
          	<li>RECOVERY_NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CreateProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| escalation_policy_id |string|✘| |
| options |[AlertOptions](project-alert-config.md#alertoptions)|✘| |
| domain_id |string|✔| |

### GetProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### ProjectAlertConfigInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_id |string | |
| options |[AlertOptions](project-alert-config.md#alertoptions) | |
| escalation_policy_info |[EscalationPolicyInfo](project-alert-config.md#escalationpolicyinfo) | |
| domain_id |string | |
| created_at |string | |

### ProjectAlertConfigQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| project_id |string|✘| |
| escalation_policy_id |string|✘| |
| domain_id |string|✔| |

### ProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| domain_id |string|✔| |

### ProjectAlertConfigStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### ProjectAlertConfigsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✔| |
| escalation_policy_id |string|✘| |
| options |[AlertOptions](project-alert-config.md#alertoptions)|✘| |
| domain_id |string|✔| |
