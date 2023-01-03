
# ViEWS partitioning

A python package for partitioning data for the ViEWS project.

## Installation

Install with pip:

```
pip install views-partitioning
```

## Usage

The partitioning package exposes functionality via the `DataPartitioner` class: 

```
from views_partitioning import DataPartitioner
```

This class wraps a nested dictionary data structure with the following general
structure:

```
{
   "A": {
      "a": (1 ,10),
      "b": (11,20)
   },
   "B": {
      "a": (1 ,20),
      "b": (21,30)
   }
}
```

The outer keys ("A", "B") denote _partitions_ while the inner keys ("a", "b")
denote _timespans_. A typical structure is to have partitions with different
_training and testing_ timespans, like so:

```
partitions = {
   "A": {
      "train": (1,100),
      "test": (101,150),
      "holdout": (151,170),
   },
   "B": {
      "train": (1,120),
      "test": (121,150),
      "holdout": (151,170),
   },
}
```

The `DataPartitioner` class can be instantiated with a python dictionary of
this form, like so:

```
partitioner = DataPartitioner(partitions)
```

The instance can then be used to subset data in the first of [two index dimensions]("https://github.com/prio-data/viewser/wiki/DataConventions):

```
a_train = partitioner("A","train",dataframe)
```

## Contributing

For information about how to contribute, see
[contributing](https://github.com/prio-data/contributing).

## Funding

The contents of this repository is the outcome of projects that have received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (Grant agreement No. 694640, *ViEWS*) and Horizon Europe (Grant agreement No. 101055176, *ANTICIPATE*; and No. 101069312, *ViEWS* (ERC-2022-POC1)), Riksbankens Jubileumsfond (Grant agreement No. M21-0002, *Societies at Risk*), Uppsala University, Peace Research Institute Oslo, the United Nations Economic and Social Commission for Western Asia (*ViEWS-ESCWA*), the United Kingdom Foreign, Commonwealth & Development Office (GSRA – *Forecasting Fatalities in Armed Conflict*), the Swedish Research Council (*DEMSCORE*), the Swedish Foundation for Strategic Environmental Research (*MISTRA Geopolitics*), the Norwegian MFA (*Conflict Trends* QZA-18/0227), and the United Nations High Commissioner for Refugees (*the Sahel Predictive Analytics project*).
