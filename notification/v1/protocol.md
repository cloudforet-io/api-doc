---
description:  
---
# Protocol

>  **Package : spaceone.api.notification.v1**

## Protocol

{% hint style="info" %}
**Protocol Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](protocol.md#create)|   [CreateProtocolRequest](protocol.md#createprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Creates a new Protocol.Protocol is the definition of which method to use when dispatching the Notifications through a Channel.When creating a protocol, you must specify the plugins provided from the repository, and you must also set the credentials to be set in the plugin if necessary. |
| 2 | [**update**](protocol.md#update)|   [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Updates a Protocol information.Update methods can update name, tags only. If you want to update plugin version or options, you can use update_plugin method. |
| 3 | [**update_plugin**](protocol.md#update_plugin)|   [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Updates a plugin for Protocol.This method is usually used when redeploying a deployed plugin container to a new version. |
| 4 | [**enable**](protocol.md#enable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Enables a Protocol.If the disabled Protocol is enabled, the Protocol can be used again and the notification can be dispatched. |
| 5 | [**disable**](protocol.md#disable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Disables a Protocol.If you disable the Protocol, the notification will not be dispatched, even if they are created. |
| 6 | [**delete**](protocol.md#delete)|   [ProtocolRequest](protocol.md#protocolrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| Delete the protocol.If there is even one channel using the protocol, it cannot be deleted. |
| 7 | [**get**](protocol.md#get)|   [GetProtocolRequest](protocol.md#getprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) | Gets a single Protocol. |
| 8 | [**list**](protocol.md#list)|   [ProtocolQuery](protocol.md#protocolquery) |   [ProtocolsInfo](protocol.md#protocolsinfo) | Lists the specified Protocols.Can search information using the query format provided by SpaceONE.Detailed information about Query format can be checked in the Search Query pages. |
| 9 | [**stat**](protocol.md#stat)|   [ProtocolStatQuery](protocol.md#protocolstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| The name of Protocol. It can have a maximum of 255 characters.|
| 2 | plugin_info |[PluginRequest](protocol.md#pluginrequest)|✅| Describe a Plugin information for protocol that include was used plugin, specific version, schema etc.|
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The tags for protocol.|
| 4 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### GetProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | protocol_id |string|✅| The ID of Protocol.|
| 2 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|
| 3 | only |list of string|❌| The list of the Protocol information column you want to be returned. It must be specified in the ProtocolInfo.|

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | The ID of plugin set in the Protocol.|
| 2 | version |string | The version of plugin.|
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | The Options that contains information about using plugin.|
| 4 | secret_id |string | The ID of the Secret containing encrypted data to be used in the plugin.|
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | The metadata of plugin. It includes schema for the data that must be set for the Channel when creating the Channel using a Protocol.The schema follows the JSON Schema format.|

### PluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | plugin_id |string|✅| The ID of plugin.|
| 2 | version |string|✅| The version of plugin.|
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The Options that contains information about using plugin.|
| 4 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The data for using plugin if necessary. This data is encrypted and stored in the Secret service.|
| 5 | schema |string|✅| The name of schema.When the secret_data is stored in the Secret service, it can be set with schema if the schema is existed.The schema is provided through the Repository service.|

### ProtocolInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">The state of Protocol.ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">{}</td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Resource type for Protocol. Currently only identity.Project or identity.User can be set.</td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The capability information for the Protocol. It included supported schema for the Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="protocol.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left">the plugin information set in Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">The tags for protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">Protocol creation time.</td>
   </tr>
  </tbody>
</table>



### ProtocolQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">Query format provided by SpaceONE. Please check the link for more information.</td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The ID of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The name of Protocol.</td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The state of Protocol. ENABLED or DISABLED only.</td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left">The type of Protocol. INTERNAL or EXTERNAL only.</td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left">The ID of domain to which the Protocol belongs.</td>
   </tr>
  </tbody>
</table>



### ProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | protocol_id |string|✅| The ID of Protocol.|
| 2 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### ProtocolStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| Statistics Query format provided by SpaceONE. Please check the link for more information.|
| 2 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### ProtocolsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProtocolInfo](protocol.md#protocolinfo) | List of queried protocols.|
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | Total counts of queried Protocols.|

### UpdateProtocolPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | protocol_id |string|✅| The ID of Protocol.|
| 2 | version |string|❌| The version of plugin you want to update. Version means the tags of plugin container image in repository that specific market place.|
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The Options that contains information about using plugin.|
| 4 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|

### UpdateProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | protocol_id |string|✅| The ID of Protocol.|
| 2 | name |string|❌| The Name of Protocol. It can have a maximum of 255 characters.|
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| The tags for protocol. When updating, existing tag information is deleted all and will be updated with new.|
| 4 | domain_id |string|✅| The ID of domain to which the Protocol belongs.|
