---
title: "Query"
linkTitle: "Query"
weight: 3
bookFlatSection: true
---
# [Query](#Query)



>  **Package : spaceone.api.core.v1**

<br>
<br>

## Query







<br>
<br>

## Message



### AggregateCount
* **name** (string)  `Required` 

    <br>

### AggregateGroup
* **keys** (AggregateGroupKey)  `Required` 

    
* **fields** (AggregateGroupField)  `Required` 

    <br>

### AggregateGroupField
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **n** (string)  `Required` 

    
* **operator** (string)  `Required` 

    
* **o** (string)  `Required` 

    
* **fields** (AggregateGroupSubField)  `Required` 

    
* **conditions** (AggregateSubCondition)  `Required` 

    <br>

### AggregateGroupKey
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **n** (string)  `Required` 

    
* **date_format** (string)  `Required` 

    <br>

### AggregateGroupSubField
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **n** (string)  `Required` 

    <br>

### AggregateProject
* **fields** (AggregateProjectField)  `Required` 

    
* **exclude_keys** (bool)  `Required` 

    <br>

### AggregateProjectField
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **n** (string)  `Required` 

    
* **operator** (string)  `Required` 

    
* **o** (string)  `Required` 

    <br>

### AggregateSort
* **key** (string)  `Required` 

    
* **desc** (bool)  `Required` 

    
* **keys** (SortKey)  `Required` 

    <br>

### AggregateSubCondition
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **value** (Value)  `Required` 

    
* **v** (Value)  `Required` 

    
* **operator** (string)  `Required` 

    
* **o** (string)  `Required` 

    <br>

### AggregateUnwind
* **path** (string)  `Required` 

    <br>

### AnalyzeQuery
* **group_by** (string)  `Required` 

    
* **field_group** (string)  `Required` 

    
* **filter** (Filter)  `Required` 

    
* **filter_or** (Filter)  `Required` 

    
* **page** (Page)  `Required` 

    
* **sort** (SortKey)  `Required` 

    
* **fields** (Struct)  `Required` 

    
* **select** (Struct)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>

### Filter
* **key** (string)  `Required` 

    
* **k** (string)  `Required` 

    
* **value** (Value)  `Required` 

    
* **v** (Value)  `Required` 

    
* **operator** (string)  `Required` 

    
* **o** (string)  `Required` 

    <br>

### Page
* **start** (uint32)  `Required` 

    
* **limit** (uint32)  `Required` 

    <br>

### Query
* **filter** (Filter)  `Required` 

    
* **filter_or** (Filter)  `Required` 

    
* **sort** (Sort)  `Required` 

    
* **page** (Page)  `Required` 

    
* **minimal** (bool)  `Required` 

    
* **count_only** (bool)  `Required` 

    
* **only** (string)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>

### Sort
* **key** (string)  `Required` 

    
* **desc** (bool)  `Required` 

    
* **keys** (SortKey)  `Required` 

    <br>

### SortKey
* **key** (string)  `Required` 

    
* **desc** (bool)  `Required` 

    <br>

### StatisticsAggregate
* **unwind** (AggregateUnwind)  `Required` 

    
* **group** (AggregateGroup)  `Required` 

    
* **count** (AggregateCount)  `Required` 

    
* **sort** (AggregateSort)  `Required` 

    
* **project** (AggregateProject)  `Required` 

    
* **limit** (int32)  `Required` 

    
* **skip** (int32)  `Required` 

    <br>

### StatisticsQuery
* **filter** (Filter)  `Required` 

    
* **filter_or** (Filter)  `Required` 

    
* **aggregate** (StatisticsAggregate)  `Required` 

    
* **page** (Page)  `Required` 

    
* **distinct** (string)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>

### TimeSeriesAnalyzeQuery
* **granularity** (Granularity)  `Required` 

    
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    
* **group_by** (string)  `Required` 

    
* **field_group** (string)  `Required` 

    
* **filter** (Filter)  `Required` 

    
* **filter_or** (Filter)  `Required` 

    
* **page** (Page)  `Required` 

    
* **sort** (SortKey)  `Required` 

    
* **fields** (Struct)  `Required` 

    
* **select** (Struct)  `Required` 

    
* **keyword** (string)  `Required` 

    <br>
