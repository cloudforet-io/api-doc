---
description:  
---
# Query

>  **Package : spaceone.api.core.v1**

## Message

### AggregateCount
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | ||

### AggregateGroup
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | keys |[AggregateGroupKey](Query.md#aggregategroupkey) | ||
| 2 | fields |[AggregateGroupField](Query.md#aggregategroupfield) | ||

### AggregateGroupField
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | k |string | ||
| 3 | name |string | ||
| 4 | n |string | ||
| 5 | operator |string | ||
| 6 | o |string | ||

### AggregateGroupKey
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | k |string | ||
| 3 | name |string | ||
| 4 | n |string | ||

### AggregateUnwind
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | path |string | ||

### Filter
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | k |string | ||
| 3 | value |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 4 | v |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | ||
| 5 | operator |string | ||
| 6 | o |string | ||

### Page
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 2 | limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### Query
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | filter |[Filter](Query.md#filter) | ||
| 2 | filter_or |[Filter](Query.md#filter) | ||
| 3 | sort |[Sort](Query.md#sort) | ||
| 4 | page |[Page](Query.md#page) | ||
| 5 | minimal |bool | ||
| 6 | count_only |bool | ||
| 7 | only |string | ||
| 8 | keyword |string | ||

### Sort
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key |string | ||
| 2 | desc |bool | ||

### StatisticsAggregate
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | unwind |[AggregateUnwind](Query.md#aggregateunwind) | ||
| 2 | group |[AggregateGroup](Query.md#aggregategroup) | ||
| 3 | count |[AggregateCount](Query.md#aggregatecount) | ||

### StatisticsQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | filter |[Filter](Query.md#filter) | ||
| 2 | filter_or |[Filter](Query.md#filter) | ||
| 3 | aggregate |[StatisticsAggregate](Query.md#statisticsaggregate) | ||
| 4 | sort |[StatisticsSort](Query.md#statisticssort) | ||
| 5 | page |[Page](Query.md#page) | ||
| 6 | limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 7 | distinct |string | ||

### StatisticsSort
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | ||
| 2 | desc |bool | ||
