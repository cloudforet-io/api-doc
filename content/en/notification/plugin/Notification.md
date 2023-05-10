---
title: "Notification"
linkTitle: "Notification"
weight: 3
bookFlatSection: true
---
# [Notification](#Notification)
A Notification is a resource delivering data from a Protocol plugin instance to a nofitication tool of an external user.


>  **Package : spaceone.api.notification.plugin**

<br>
<br>

## Notification





**Notification Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**dispatch**](./Notification#dispatch) | [PluginDispatchRequest](Notification#plugindispatchrequest) | [Empty](./Notification#empty) |



    
<br>

### dispatch

Dispatches data from Cloudforet to a specific notification Protocol. When dispatching data, data input by a User is included in the `options` parameter, and `notification` information to be delivered is included in the `message` parameter. Also, data dispatched includes basic information such as `notification_type` and `secret_data`.







 {{< tabs " dispatch " >}}

 {{< tab "Request Example" >}}



[PluginDispatchRequest](./Notification#plugindispatchrequest)

* **options** (Struct)  `Required` 

  *Option value required for notification delivery.*


* **message** (Struct)  `Required` 

  *Message containing notification information*


* **notification_type** (NotificationType)  `Required` 

  *The type of Notification*


* **secret_data** (Struct)  `Required` 

  *Secret value required for notification delivery.
The secret data usually includes the credential information required for the plugin to access the external system.*


* **channel_data** (Struct)  `Required` 

  *Channel data required for notification delivery.*





{{< highlight json >}}
{
   "options": {},
   "message": {
   "tags": [
       {
           "key": "Alert Number",
           "options": {"short": true},
           "value": "#108664"
       },
       {
           "options": {"short": true},
           "key": "State",
           "value": "TRIGGERED"
       },
       {
           "value": "LOW",
           "options": {"short": true},
           "key": "Urgency"
       },
       {
           "value": "kubectl-webhook",
           "key": "Triggered by",
           "options": {"short": true}
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
   "callbacks": [{
       "url": "https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/alert/alert-x1v2c3v456/8f2ede36213dqw4d7d5awe07ds32d883/ACKNOWLEDGED",
       "label": "Acknowledge Alerts"}],
   "link": "https://spaceone.console.dev.spaceone.dev/alert-manager/alert/alert-x1v2c3v456",
   "title": "[Alerting] Notification of access to the SpaceONE",
   "description": "SSH Access to spaceone-api from admin"},
   "notification_type": "INFO",
   "secret_data": "********",
   "channel_data": {"email": "test5@test.com"}
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    


<br>
<br>

## Message



### PluginDispatchRequest
* **options** (Struct)  `Required` 

  *Option value required for notification delivery.*

    
* **message** (Struct)  `Required` 

  *Message containing notification information*

    
* **notification_type** (NotificationType)  `Required` 

  *The type of Notification*

    
* **secret_data** (Struct)  `Required` 

  *Secret value required for notification delivery.
The secret data usually includes the credential information required for the plugin to access the external system.*

    
* **channel_data** (Struct)  `Required` 

  *Channel data required for notification delivery.*

    <br>
