---
description: A Notification is a resource delivering data from a Protocol plugin instance to a nofitication tool of an external user.
---
# Notification

>  **Package : spaceone.api.notification.plugin**

## Notification

{% hint style="info" %}
**Notification Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**dispatch**](notification.md#dispatch)|   [PluginDispatchRequest](notification.md#plugindispatchrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### dispatch

> Dispatches data from Cloudforet to a specific notification Protocol. When dispatching data, data input by a User is included in the `options` parameter, and `notification` information to be delivered is included in the `message` parameter. Also, data dispatched includes basic information such as `notification_type` and `secret_data`.

| Type | Message |
| :--- | :--- |
| Request | [PluginDispatchRequest](notification.md#plugindispatchrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "options": {},
    "message": {
        "tags": [
            {
                "key": "Alert Number",
                "options": {
                    "short": true
                },
                "value": "#108664"
            },
            {
                "options": {
                    "short": true
                },
                "key": "State",
                "value": "TRIGGERED"
            },
            {
                "value": "LOW",
                "options": {
                    "short": true
                },
                "key": "Urgency"
            },
            {
                "value": "kubectl-webhook",
                "key": "Triggered by",
                "options": {
                    "short": true
                }
            },
            {
                "value": "SpaceONE > Project1",
                "key": "Project"
            },
            {
                "value": "spaceone-api",
                "key": "Resource"
            }
        ],
        "occurred_at": "2022-06-27T09:22:57.967Z",
        "callbacks": [
            {
                "url": "https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-x1v2c3v456/8f2ede36213dqw4d7d5awe07ds32d883/ACKNOWLEDGED",
                "label": "Acknowledge Alerts"
            }
        ],
        "link": "https://spaceone.console.dev.spaceone.dev/alert-manager/alert/alert-x1v2c3v456",
        "title": "[Alerting] Notification of access to the SpaceONE",
        "description": "SSH Access to spaceone-api from admin"
    },
    "notification_type": "INFO",
    "secret_data": "********",
    "channel_data": {
        "email": "test5@test.com"
    }
}
```
{% endtab %}
{% endtabs %}


## 

## Message

### PluginDispatchRequest
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
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Option value required for notification delivery.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Message containing notification information</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>INFO</li>
          	<li>ERROR</li>
          	<li>SUCCESS</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The type of Notification</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Secret value required for notification delivery.The secret data usually includes the credential information required for the plugin to access the external system.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">channel_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Channel data required for notification delivery.</td>
   </tr>
  </tbody>
</table>


