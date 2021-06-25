# Open Data Dataset Description

The REaltime DAta Synthesis and Analysis (REDASA) COVID-19 snapshot contains the output of the curation protocol produced by our curator community. A detailed description can be found in [our paper](https://www.jmir.org/2021/5/e25714). The first S3 bucket listed in Resources contains a large collection of medical documents in text format extracted from the [CORD-19 dataset](https://registry.opendata.aws/cord-19/), plus other sources deemed relevant by the REDASA consortium. The second S3 bucket contains a series of documents surfaced by [Amazon Kendra](https://aws.amazon.com/kendra/) that were considered relevant for each medical question asked. The final S3 bucket contains the GroundTruth annotations created by our curator community.
  
## Resource description

### Curation Raw Documents

**ARN:** arn:aws:s3:::pansurg-curation-raw-open-data

This s3 bucket contains a collection of raw documents, mostly in text format, which should be Markdown compatible.

- cord19/ prefix contains data from the CORD-19 corpus, either extracted from [AWS CORD-19](https://cord19.aws/) snapshot or [directly downloaded](https://allenai.org/data/cord-19) from their release version. The documents are postprocess and transformed into the txt format allowing further indexing with [Amazon Kendra](https://aws.amazon.com/kendra/).
- cwtest/ and mwtest/ contain datasets that have been identified by the REDASA projects in formats other than txt (.csv, .pdf, .json)
- webcrawl/ contains documents extracted by [our crawler](https://www.jmir.org/2021/5/e25714) from sources identified by the REDASA project. The list contains national guidelines on COVID-19 in various languages, medical response guideline by other international organisations (i.e. NICE, IHME, etc).

### Kendra queries and responses

**ARN:** arn:aws:s3:::pansurg-curation-workflo-kendraqueryresults50d0eb-open-data

For all the questions curated during the REDASA project, we created a Kendra index. The documents available in this S3 bucket were surfaced by the Kendra index as being relevant to the research medical question.

The documents are groupped by question, so redasa1-Q\[q\]-\[nn\] where q represent the question number, nn is the number of documents retrieved. More details about the medical research questions is described in [our paper](https://www.jmir.org/2021/5/e25714).

### Curation results

**ARN:** arn:aws:s3:::pansurg-curation-final-curations-open-data

An S3 bucket that contains the final curation data in GroundTruth format.

The documents are groupped by question and stint, so REDASA-q\[q\]-s\[s\] where q represent the question number, s is the stint (round) number. More details about the protocol is described in [our paper](https://www.jmir.org/2021/5/e25714).

## Quick tutorial on using the data

A quick tutorial on using and data visualisation is available in the [Readme](README.md) file.
