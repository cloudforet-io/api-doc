---
description: An Alert, a set of Events, is the smallest unit to manage incidents.
---
# Alert

>  **Package : spaceone.api.monitoring.v1**

## Alert

{% hint style="info" %}
**Alert Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](alert.md#create)|   [CreateAlertRequest](alert.md#createalertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**update**](alert.md#update)|   [UpdateAlertRequest](alert.md#updatealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**update_state**](alert.md#update_state)|   [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |   [AlertInfo](alert.md#alertinfo) |
| [**merge**](alert.md#merge)|   [MergeAlertRequest](alert.md#mergealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**snooze**](alert.md#snooze)|   [SnoozeAlertRequest](alert.md#snoozealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**add_responder**](alert.md#add_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**remove_responder**](alert.md#remove_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**add_project_dependency**](alert.md#add_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**remove_project_dependency**](alert.md#remove_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**delete**](alert.md#delete)|   [AlertRequest](alert.md#alertrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](alert.md#get)|   [GetAlertRequest](alert.md#getalertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**list**](alert.md#list)|   [AlertQuery](alert.md#alertquery) |   [AlertsInfo](alert.md#alertsinfo) |
| [**stat**](alert.md#stat)|   [AlertStatQuery](alert.md#alertstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/alerts
>

> Creates a new Alert. Alerts generated with `create` method are made in a manual way. Manually made Alerts can be used for Notifications.

| Type | Message |
| :--- | :--- |
| Request | [CreateAlertRequest](alert.md#createalertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "title": "sample test",
    "description": "This is a description of sample.",
    "urgency": "HIGH",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "alert_number": 104053,
    "alert_id": "alert-123456789012",
    "title": "sample test",
    "state": "TRIGGERED",
    "description": "This is a description of sample.",
    "urgency": "HIGH",
    "severity": "NONE",
    "escalation_step": 1,
    "additional_info": {},
    "triggered_by": "user1@email.com",
    "escalation_policy_id": "ep-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T01:43:08.566Z",
    "updated_at": "2022-01-01T01:43:08.566Z",
    "escalated_at": "2022-01-01T01:43:54.464Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /monitoring/v1/alert/{alert_id}
>

> Updates a specific Alert. You can make changes in Alert settings, including the `title`, `description`, `responder`, `state`, and `urgency`. The `responder` of the Alert is a User who is assigned to respond to the Alert.

| Type | Message |
| :--- | :--- |
| Request | [UpdateAlertRequest](alert.md#updatealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "state": "ACKNOWLEDGED",
    "urgency": "LOW",
    "description": "[updating]This is a description of sample.",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "alert_number": 104053,
    "alert_id": "alert-123456789012",
    "title": "sample test",
    "state": "ACKNOWLEDGED",
    "description": "[updating]This is a description of sample. ",
    "urgency": "LOW",
    "severity": "NONE",
    "escalation_step": 1,
    "additional_info": {},
    "triggered_by": "user1@email.com",
    "escalation_policy_id": "ep-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T01:43:08.566Z",
    "updated_at": "2022-01-01T01:43:08.566Z",
    "acknowledged_at": "2022-01-01T01:48:52.799Z",
    "escalated_at": "2022-01-01T01:43:54.464Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_state
> **POST** /monitoring/v1/alert/{alert_id}/{access_key}/{state}
>

> Updates the state of an Alert via callback URL by creating a temporary `access_key` while generating a Notification about the Alert.

| Type | Message |
| :--- | :--- |
| Request | [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "access_key": "1q2w3e4r5t6y7u8i9o0p",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### merge
> **POST** /monitoring/v1/alerts/merge
>


| Type | Message |
| :--- | :--- |
| Request | [MergeAlertRequest](alert.md#mergealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### snooze
> **POST** /monitoring/v1/alert/{alert_id}/snooze
>


| Type | Message |
| :--- | :--- |
| Request | [SnoozeAlertRequest](alert.md#snoozealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### add_responder
> **POST** /monitoring/v1/alert/{alert_id}/responders
>

> Adds a responder who receives a Notification about an Alert.

| Type | Message |
| :--- | :--- |
| Request | [AlertResponderRequest](alert.md#alertresponderrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "resource_type": "identity.User",
    "resource_id": "user2@email.com",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "alert_number": 104053,
    "alert_id": "alert-123456789012",
    "title": "sample test",
    "state": "ACKNOWLEDGED",
    "description": "[updating]This is a description of sample. ",
    "urgency": "LOW",
    "severity": "NONE",
    "escalation_step": 1,
    "responders": [
        {
            "resource_type": "identity.User",
            "resource_id": "user2@email.com"
        }
    ],
    "additional_info": {},
    "triggered_by": "user1@email.com",
    "escalation_policy_id": "ep-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T01:43:08.566Z",
    "updated_at": "2022-01-01T01:43:08.566Z",
    "acknowledged_at": "2022-01-01T02:24:12.051Z",
    "escalated_at": "2022-01-01T01:43:54.464Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### remove_responder
> **DELETE** /monitoring/v1/alert/{alert_id}/responders
>

> Deletes a responder who receives a Notification about an Alert.

| Type | Message |
| :--- | :--- |
| Request | [AlertResponderRequest](alert.md#alertresponderrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "resource_type": "identity.User",
    "resource_id": "user2@email.com",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "alert_number": 104053,
    "alert_id": "alert-123456789012",
    "title": "sample test",
    "state": "ACKNOWLEDGED",
    "description": "[updating]This is a description of sample. ",
    "urgency": "LOW",
    "severity": "NONE",
    "escalation_step": 1,
    "additional_info": {},
    "triggered_by": "user1@email.com",
    "escalation_policy_id": "ep-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T01:43:08.566Z",
    "updated_at": "2022-01-01T01:43:08.566Z",
    "acknowledged_at": "2022-01-01T01:48:52.799Z",
    "escalated_at": "2022-01-01T01:43:54.464Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### add_project_dependency
> **POST** /monitoring/v1/alert/{alert_id}/project-dependencies
>


| Type | Message |
| :--- | :--- |
| Request | [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### remove_project_dependency
> **DELETE** /monitoring/v1/alert/{alert_id}/project-dependency/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/alert/{alert_id}
>

> Deletes a specific Alert and remove it from the list of Alerts. You must specify the `alert_id` of the Alert to delete.

| Type | Message |
| :--- | :--- |
| Request | [AlertRequest](alert.md#alertrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /monitoring/v1/alert/{alert_id}
>

> Gets a specific Alert. Prints detailed information about the Alert.

| Type | Message |
| :--- | :--- |
| Request | [GetAlertRequest](alert.md#getalertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "alert_id": "alert-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "alert_number": 104053,
    "alert_id": "alert-123456789012",
    "title": "sample test",
    "state": "ACKNOWLEDGED",
    "description": "[updating]This is a description of sample. ",
    "urgency": "LOW",
    "severity": "NONE",
    "escalation_step": 1,
    "additional_info": {},
    "triggered_by": "user1@email.com",
    "escalation_policy_id": "ep-123456789012",
    "project_id": "project-123456789012",
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T01:43:08.566Z",
    "updated_at": "2022-01-01T01:43:08.566Z",
    "acknowledged_at": "2022-01-01T01:48:52.799Z",
    "escalated_at": "2022-01-01T01:43:54.464Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/alerts
>
> **POST** /monitoring/v1/alerts/search


> Gets a list of all Alerts. You can use a query to get a filtered list of Alerts.

| Type | Message |
| :--- | :--- |
| Request | [AlertQuery](alert.md#alertquery) |
| Response |  [AlertsInfo](alert.md#alertsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "alert_number": 104057,
            "alert_id": "alert-987654321098",
            "title": "Notification of access to the bastion Host",
            "state": "TRIGGERED",
            "description": "SSH Access to stargate-dev from adm",
            "urgency": "LOW",
            "severity": "INFO",
            "resource": {
                "resource_id": "server-123456789012",
                "resource_type": "inventory.Server",
                "name": "stargate-dev"
            },
            "escalation_step": 1,
            "escalation_ttl": 1,
            "additional_info": {
                "host": "[]",
                "user": "user1"
            },
            "triggered_by": "webhook-123456789012",
            "webhook_id": "webhook-123456789012",
            "escalation_policy_id": "ep-123456789012",
            "project_id": "project-123456789012",
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T02:46:35.934Z",
            "updated_at": "2022-01-01T02:46:35.934Z",
            "escalated_at": "2022-01-01T02:46:35.979Z"
        },
        {
            "alert_number": 104056,
            "alert_id": "alert-123456789999",
            "title": "Notification of access to the bastion Host",
            "state": "TRIGGERED",
            "description": "SSH Access to stargate-dev from user3@email.com",
            "urgency": "LOW",
            "severity": "INFO",
            "resource": {
                "resource_id": "server-123456789012",
                "resource_type": "inventory.Server",
                "name": "stargate-dev"
            },
            "escalation_step": 1,
            "escalation_ttl": 1,
            "additional_info": {
                "user": "user3@email.com",
                "host": "['111.111.111.11']"
            },
            "triggered_by": "webhook-123456789012",
            "webhook_id": "webhook-123456789012",
            "escalation_policy_id": "ep-123456789012",
            "project_id": "project-123456789012",
            "domain_id": "domain-123456789012",
            "created_at": "2022-01-01T02:46:31.391Z",
            "updated_at": "2022-01-01T02:46:31.391Z",
            "escalated_at": "2022-01-01T02:46:31.553Z"
        }
    ],
    "total_count": 21283
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/alerts/stat
>


| Type | Message |
| :--- | :--- |
| Request | [AlertStatQuery](alert.md#alertstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AlertInfo
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
      <td style="text-align:left; width:100px;">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">rule</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource</td>
      <td style="text-align:left"><a href="alert.md#alertresource">AlertResource</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_snoozed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">snoozed_end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_step</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_ttl</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">responders</td>
      <td style="text-align:left"><a href="alert.md#alertresponder">list of AlertResponder</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_dependencies</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">additional_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
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
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">acknowledged_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resolved_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AlertProjectDependencyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| project_id |string|✔| |
| domain_id |string|✔| |

### AlertQuery
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
      <td style="text-align:left; width:100px;">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_snoozed</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">webhook_id</td>
      <td style="text-align:left">string</td>
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



### AlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| domain_id |string|✔| |

### AlertResource
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| resource_type |string | |
| name |string | |

### AlertResponder
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| resource_id |string | |

### AlertResponderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| resource_type |string|✔| |
| resource_id |string|✔| |
| domain_id |string|✔| |

### AlertStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### AlertsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of AlertInfo](alert.md#alertinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAlertRequest
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
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
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



### GetAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MergeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alerts |list of string|✔| |
| merge_to |string|✔| |
| domain_id |string|✔| |

### SnoozeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| end_time |string|✔| |
| domain_id |string|✔| |

### UpdateAlertRequest
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
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
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
      <td style="text-align:left; width:100px;">reset_status_message</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_description</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_assignee</td>
      <td style="text-align:left">bool</td>
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



### UpdateAlertStateRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| access_key |string|✔| |
| state |string|✘| |
