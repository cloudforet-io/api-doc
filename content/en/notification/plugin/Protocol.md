---
title: "Protocol"
linkTitle: "Protocol"
weight: 3
bookFlatSection: true
---
# [Protocol](#Protocol)
desc: A Protocol is a plugin instance defining how a User receives data from Cloudforet.


>  **Package : spaceone.api.notification.plugin**

<br>
<br>

## Protocol


**Protocol Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](./Protocol#init) | [InitRequest](Protocol#initrequest) | [PluginInfo](./Protocol#plugininfo) |
| [**verify**](./Protocol#verify) | [PluginVerifyRequest](Protocol#pluginverifyrequest) | [Empty](./Protocol#empty) |



    
<br>

### init




 {{< tabs " init " >}}




{{< /tabs >}}

    
<br>

### verify




 {{< tabs " verify " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### InitRequest
* **options** (Struct)  `Required` 

  *is_required: true
desc: Option value used when initializing the plugin.*

    <br>

### PluginInfo
* **metadata** (Struct)  `Required` 

  *desc: Metadata value required to input various values required for plugin to work.
Metadata value required to input various values required for plugin to work.
In the case of protocol plugins, when creating a channel, the plugin contains the definition of additional data (channel data) required for channel transmission.*

    <br>

### PluginVerifyRequest
* **options** (Struct)  `Required` 

  *is_required: true
desc: Option values required for the plugin to work.*

    
* **secret_data** (Struct)  `Required` 

  *is_required: true
desc: The secret value required for the plugin to work.
The secret data usually includes the credential information required for the plugin to access the external system.*

    <br>
