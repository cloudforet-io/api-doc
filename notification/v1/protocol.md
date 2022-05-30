---
description:  
---
# Protocol

>  **Package : spaceone.api.notification.v1**

## Protocol

{% hint style="info" %}
**Protocol Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](protocol.md#create)|   [CreateProtocolRequest](protocol.md#createprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Creates a new Protocol.Protocol is the definition of which method to use when dispatching the Notifications through a Channel.When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary. |
| [**update**](protocol.md#update)|   [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Updates a Protocol information.Update methods can update name, tags only. If you want to update plugin version or options, you can use update_plugin method. |
| [**update_plugin**](protocol.md#update_plugin)|   [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Updates a plugin for Protocol.This method is usually used when redeploying a deployed plugin container to a new version. |
| [**enable**](protocol.md#enable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Enables a Protocol.If the disabled Protocol is enabled, the Protocol can be used again and the notification can be dispatched. |
| [**disable**](protocol.md#disable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Disables a Protocol.If you disable the Protocol, the notification will not be dispatched, even if they are created. |
| [**delete**](protocol.md#delete)|   [ProtocolRequest](protocol.md#protocolrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Delete the protocol.If there is even one channel using the protocol, it cannot be deleted. |
| [**get**](protocol.md#get)|   [GetProtocolRequest](protocol.md#getprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Gets a single Protocol. |
| [**list**](protocol.md#list)|   [ProtocolQuery](protocol.md#protocolquery) |   [ProtocolsInfo](protocol.md#protocolsinfo) | Lists the specified Protocols.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| [**stat**](protocol.md#stat)|   [ProtocolStatQuery](protocol.md#protocolstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Creates a new Protocol.Protocol is the definition of which method to use when dispatching the Notifications through a Channel.When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Updates a Protocol information.Update methods can update name, tags only. If you want to update plugin version or options, you can use update_plugin method.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update_plugin</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateProtocolPluginRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Updates a plugin for Protocol.This method is usually used when redeploying a deployed plugin container to a new version.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">enable</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Enables a Protocol.If the disabled Protocol is enabled, the Protocol can be used again and the notification can be dispatched.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">disable</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Disables a Protocol.If you disable the Protocol, the notification will not be dispatched, even if they are created.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Delete the protocol.If there is even one channel using the protocol, it cannot be deleted.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetProtocolRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Gets a single Protocol.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">Lists the specified Protocols.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.</td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProtocolStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
### create
> **POST** /notification/v1/protocols
>

> Creates a new Protocol.Protocol is the definition of which method to use when dispatching the Notifications through a Channel.When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary.

| Type | Message |
| :--- | :--- |
| Request | [CreateProtocolRequest](protocol.md#createprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### update
> **PUT** /notification/v1/protocol/{protocol_id}
>

> Updates a Protocol information.Update methods can update name, tags only. If you want to update plugin version or options, you can use update_plugin method.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### update_plugin
> **PUT** /notification/v1/protocol/{protocol_id}/plugin
>

> Updates a plugin for Protocol.This method is usually used when redeploying a deployed plugin container to a new version.

| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/protocol/{protocol_id}/enable
>

> Enables a Protocol.If the disabled Protocol is enabled, the Protocol can be used again and the notification can be dispatched.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/protocol/{protocol_id}/disable
>

> Disables a Protocol.If you disable the Protocol, the notification will not be dispatched, even if they are created.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/protocol/{protocol_id}
>

> Delete the protocol.If there is even one channel using the protocol, it cannot be deleted.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/protocol/{protocol_id}
>

> Gets a single Protocol.

| Type | Message |
| :--- | :--- |
| Request | [GetProtocolRequest](protocol.md#getprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### list
> **GET** /notification/v1/protocols
>
> **POST** /notification/v1/protocols/search


> Lists the specified Protocols.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages.

| Type | Message |
| :--- | :--- |
| Request | [ProtocolQuery](protocol.md#protocolquery) |
| Response |  [ProtocolsInfo](protocol.md#protocolsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/protocols/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolStatQuery](protocol.md#protocolstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| The name of Protocol. It can have a maximum of 255 characters.|
| plugin_info |[PluginRequest](protocol.md#pluginrequest)|✅| Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The tags for protocol.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### GetProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| The ID of Protocol.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|
| only |list of string|❌| The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.|

### PluginInfo
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
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of plugin set in the Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The version of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The Options that contains information about using plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of the Secret containing encrypted data to be used in the plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The metadata of plugin. It includes schema for the data that must be set for the Channel when creating the Channel using a Protocol.The schema follows the JSON Schema format.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:left">Auto upgrade for plugin.If the upgrade_mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.</td>
   </tr>
  </tbody>
</table>



### PluginRequest
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
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The version of plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The Options that contains information about using plugin.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The data for using plugin if necessary. This data is encrypted and stored in the Secret service.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The name of schema.When the secret_data is stored in the Secret service, it can be set with schema if the schema is existed.The schema is provided through the Repository service.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left">Auto upgrade feature for plugin.If the upgrade mode is AUTO, check the latest plugin version when running the plugin, and if a new version is existed, replace the plugin and then run it.</td>
   </tr>
  </tbody>
</table>



### ProtocolInfo
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
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">The state of Protocol.ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">{}</td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Resource type for Protocol. Currently only identity.Project or identity.User can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The capability information for the Protocol. It included supported schema for the Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="protocol.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left">the plugin information set in Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The tags for protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Protocol creation time.</td>
   </tr>
  </tbody>
</table>



### ProtocolQuery
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
<td style="text-align:center">❌</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The state of Protocol. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The type of Protocol. INTERNAL or EXTERNAL only.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
  </tbody>
</table>



### ProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| The ID of Protocol.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### ProtocolStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### ProtocolsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProtocolInfo](protocol.md#protocolinfo) | List of queried protocols.|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Protocols.|

### UpdateProtocolPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| The ID of Protocol.|
| version |string|❌| The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.|
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The Options that contains information about using plugin.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### UpdateProtocolRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| protocol_id |string|✅| The ID of Protocol.|
| name |string|❌| The Name of Protocol. It can have a maximum of 255 characters.|
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.|
| domain_id |string|✅| The ID of domain to which the Protocol belongs.|
