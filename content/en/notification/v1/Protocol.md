---
title: "Protocol"
linkTitle: "Protocol"
weight: 3
bookFlatSection: true
---
# [Protocol](#Protocol)
desc: A Protocol defines the method to use when dispatching Notifications via a channel.


>  **Package : spaceone.api.notification.v1**

<br>
<br>

## Protocol


**Protocol Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Protocol#create) | [CreateProtocolRequest](Protocol#createprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**update**](./Protocol#update) | [UpdateProtocolRequest](Protocol#updateprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**update_plugin**](./Protocol#update_plugin) | [UpdateProtocolPluginRequest](Protocol#updateprotocolpluginrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**enable**](./Protocol#enable) | [ProtocolRequest](Protocol#protocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**disable**](./Protocol#disable) | [ProtocolRequest](Protocol#protocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**delete**](./Protocol#delete) | [ProtocolRequest](Protocol#protocolrequest) | [Empty](./Protocol#empty) |
| [**get**](./Protocol#get) | [GetProtocolRequest](Protocol#getprotocolrequest) | [ProtocolInfo](./Protocol#protocolinfo) |
| [**list**](./Protocol#list) | [ProtocolQuery](Protocol#protocolquery) | [ProtocolsInfo](./Protocol#protocolsinfo) |
| [**stat**](./Protocol#stat) | [ProtocolStatQuery](Protocol#protocolstatquery) | [Struct](./Protocol#struct) |



    
<br>

### create

> **POST** /notification/v1/protocol/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /notification/v1/protocol/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### update_plugin

> **POST** /notification/v1/protocol/update-plugin
>




 {{< tabs " update_plugin " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /notification/v1/protocol/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /notification/v1/protocol/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /notification/v1/protocol/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /notification/v1/protocol/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /notification/v1/protocol/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /notification/v1/protocol/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateProtocolRequest
* **name** (string)  `Required` 

  *is_required: true
desc: The name of Protocol. It can have a maximum of 255 characters.*

    
* **plugin_info** (PluginRequest)  `Required` 

  *is_required: true
desc: Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for protocol.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>

### GetProtocolRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    
* **only** (string)  `Required` 

  *is_required: false
desc: The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.*

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

  *desc: The ID of plugin set in the Protocol.*

    
* **version** (string)  `Required` 

  *desc: The version of plugin.*

    
* **options** (Struct)  `Required` 

  *desc: The Options that contains information about using plugin.*

    
* **secret_id** (string)  `Required` 

  *desc: The ID of the Secret containing encrypted data to be used in the plugin.*

    
* **metadata** (Struct)  `Required` 

  *desc: The metadata of plugin. It includes schema for the data that must be set for the Channel when creating the Channel using a Protocol.
The schema follows the JSON Schema format.*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *desc: Auto upgrade for plugin.
If the upgrade_mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.*

    <br>

### PluginRequest
* **plugin_id** (string)  `Required` 

  *is_required: true
desc: The ID of plugin.*

    
* **version** (string)  `Required` 

  *is_required: true
desc: The version of plugin.*

    
* **options** (Struct)  `Required` 

  *is_required: false
desc: The Options that contains information about using plugin.*

    
* **secret_data** (Struct)  `Required` 

  *is_required: false
desc: The data for using plugin if necessary. This data is encrypted and stored in the Secret service.*

    
* **schema** (string)  `Required` 

  *is_required: false
desc: The name of schema.
When the secret_data is stored in the Secret service, it can be set with schema if the schema is existed.
The schema is provided through the Repository service.*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *is_required: false
desc: Auto upgrade feature for plugin.
If the upgrade mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.*

    <br>

### ProtocolInfo
* **protocol_id** (string)  `Required` 

  *desc: The ID of Protocol.*

    
* **name** (string)  `Required` 

  *desc: The name of Protocol.*

    
* **state** (ProtocolState)  `Required` 

  *desc: The state of Protocol.
ENABLED or DISABLED only.*

    
* **protocol_type** (ProtocolType)  `Required` 

  *desc : The type of Protocol.
INTERNAL or EXTERNAL only.*

    
* **resource_type** (string)  `Required` 

  *desc : Resource type for Protocol. Currently only identity.Project or identity.User can be set.*

    
* **capability** (Struct)  `Required` 

  *desc : The capability information for the Protocol. It included supported schema for the Protocol.*

    
* **plugin_info** (PluginInfo)  `Required` 

  *desc: the plugin information set in Protocol.*

    
* **tags** (Struct)  `Required` 

  *desc: The tags for protocol.*

    
* **domain_id** (string)  `Required` 

  *desc: The ID of domain to which the Protocol belongs.*

    
* **created_at** (string)  `Required` 

  *desc: Protocol creation time.*

    <br>

### ProtocolQuery
* **query** (Query)  `Required` 

  *is_required: false
desc: Query format provided by SpaceONE. Please check the link for more information.*

    
* **protocol_id** (string)  `Required` 

  *is_required: false
desc: The ID of Protocol.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The name of Protocol.*

    
* **state** (ProtocolState)  `Required` 

  *is_required: false
desc: The state of Protocol. ENABLED or DISABLED only.*

    
* **protocol_type** (ProtocolType)  `Required` 

  *is_required: false
desc: The type of Protocol. INTERNAL or EXTERNAL only.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>

### ProtocolRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of Protocol.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>

### ProtocolStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true
desc: Statistics Query format provided by SpaceONE. Please check the link for more information.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>

### ProtocolsInfo
* **results** (ProtocolInfo)  `Required` 

  *desc: List of queried protocols.*

    
* **total_count** (int32)  `Required` 

  *desc: Total counts of queried Protocols.*

    <br>

### UpdateProtocolPluginRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of Protocol.*

    
* **version** (string)  `Required` 

  *is_required: false
desc: The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.*

    
* **options** (Struct)  `Required` 

  *is_required: false
desc: The Options that contains information about using plugin.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>

### UpdateProtocolRequest
* **protocol_id** (string)  `Required` 

  *is_required: true
desc: The ID of Protocol.*

    
* **name** (string)  `Required` 

  *is_required: false
desc: The Name of Protocol. It can have a maximum of 255 characters.*

    
* **tags** (Struct)  `Required` 

  *is_required: false
desc: The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.*

    
* **domain_id** (string)  `Required` 

  *is_required: true
desc: The ID of domain to which the Protocol belongs.*

    <br>
