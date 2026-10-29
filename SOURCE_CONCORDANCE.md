# Source-edition preflight: relativistic tearing-mediated turbulence

## Verified target and reading

Stanislav Boldyrev and Nuno F. Loureiro, **Tearing-mediated Alfvénic
Turbulence in a Relativistic Plasma**, *The Astrophysical Journal* **979**(2),
232 (11 pages), DOI [10.3847/1538-4357/ada28a](https://doi.org/10.3847/1538-4357/ada28a).

The supplied PDF was independently hashed and its actual page tree counted:

- 517,337 bytes; 11 pages.
- SHA-256 `c03eb1d83e8f01c3c7283973ed0a6d0b545b7b30ecc7c53b2996e039b9e1c1f6`.
- Embedded producer/creator: IOPP. Its first page has the journal citation,
  DOI, publisher copyright and CC BY 4.0 notice, matching title/authors, and
  the received/revised/accepted/published sequence.
- Received 11 November 2024; revised 18 December 2024; accepted
  19 December 2024; published online 29 January 2025. Issue date is
  1 February 2025, a different date from online publication.

All 11 supplied pages were read completely, including both figure
captions, footnotes, acknowledgments, Appendix A.1-A.5, ORCIDs and all
references. All 11 pages were also visually inspected at the cached
130-dpi renders. No scientific error was presumed in this preflight.

## Human-cleared publisher content and unresolved byte comparison

The [primary Crossref record](https://api.crossref.org/works/10.3847/1538-4357/ada28a)
returned HTTP 200 and confirms the authors, title, journal, volume, issue,
article number and dates. Its publisher links identify the article/PDF as
`vor`, and its license record specifies CC BY 4.0. Metadata bytes are
recorded as `crossref-ada28a.json`, SHA-256
`b7859e49bb5d7ec8947edd924a80c86140424356abab79797e5405cfd4ac1062`.

An earlier ordinary anonymous request to the official
[article PDF](https://iopscience.iop.org/article/10.3847/1538-4357/ada28a/pdf)
redirected to a Perfdrive human-verification page. The response was HTML,
even though its HTTP status was 200. It was not accepted as a PDF. No
challenge bypass, browser interaction or repeated request was attempted.
The safe `publisher-access.json` omits transient redirect queries and
network-address information. This is retained as a true **historical**
fetch observation, not the current access status.

The user subsequently completed the human check. The ordinary publisher
full article is now visible in the browser. The parent saved the exact
text content of all 149 publisher `math/tex` script nodes as
`journal-browser-math-tex.json`, SHA-256
`91db428fd02ef93bb27f254821991e89405489a7953d624d1743c0d597af2c83`.
This reviewer read those nodes and checked every one of the 78 numbered
display expressions against the supplied PDF's page pixels. No
substantive mathematical difference was identified. The page-linked
comparison is `journal-display-equations.json`, SHA-256
`649cacfc97a35b435067f3805f26d9c2a360992664ff679547ce27cb0d78cf39`.
This is publisher-generated script text, not an author-source TeX archive.

Accordingly, the supplied file is internally identifiable as the
journal-formatted version of record, and its bibliography agrees with the
primary metadata. **A fresh official publisher PDF has not yet been
downloaded, so exact byte identity with the currently served publisher
file is unverified.** The human block is resolved for live HTML and
machine mathematics; a new PDF download has simply not been identified.
The checked mathematical agreement does not imply binary identity or an
independent comparison of every word of official HTML prose.

| Candidate edition | What was established | Byte/content comparison |
|---|---|---|
| Supplied IOP journal PDF | Full 11-page reading; VOR citation/production/date/license identifiers | Actual size/hash recorded |
| Official publisher VOR endpoint | Current full HTML is human-cleared; all 78 display formulas match the supplied pages | Fresh PDF bytes not obtained; binary comparison pending |
| Target arXiv preprint | No authentic identifier established in the bounded primary discovery below | No version history or differences invented |

## Bounded arXiv and correction discovery

Official arXiv API queries were accessible:

1. `all:"Tearing-mediated" AND all:"relativistic"` returned one unrelated
   2026 paper, not this target.
2. `au:Boldyrev AND au:Loureiro`, sorted by submission date, requested up
   to 100 records and returned 14, newest submitted in April 2021. None
   was this target.

Responses and safe receipts are retained as `arxiv-query.xml` and
`arxiv-coauthors-query.xml` with corresponding receipt JSONs. The latter
response SHA-256 is
`a82753d5f4e60b8fb15b256809177555a5ca8e42489a8e07712bf30dd83effa1`.
These finite queries and title searches do **not** prove that no preprint
exists. No target arXiv PDF/source archive was downloaded. The
`arxiv.org/abs/2410.16167` link in the supplied references belongs to
Demidov and Lyubarsky, not to this paper.

Crossref's relation object is empty and has no `update-to`/`updated-by`
field. The separate bounded title/DOI correction and deposit searches
identified no target-specific correction, erratum or response, and no
authentic target-linked public software/data deposit. That context check
predates human clearance; it could not inspect publisher update and
availability headings. The current browser is accessible, but this
reviewer has not yet read those headings from a saved main-text capture.
These are bounded negative observations, not an exhaustive absence claim.
The historical independent context record is
`correction-and-deposit-check.json`, SHA-256
`e91949edb841e34ac6ec15ca869467436372a8a5e5232aa414916ac174ea6251`.

## Mathematical and figure locator map

This is an analytical reduced-fluid and turbulence-scaling paper, not a
report of a new PIC simulation. It uses two illustrative figures:

- Figure 1, p.7: numerical solution of inner ODE (A5), with
  beta_s=1, lambda=10^(-4), d_rel/a=10^(-2), compared with asymptotic
  solutions (A8)/(A13) and (A10)/(A14).
- Figure 2, p.8: a **sketch** of Harris-profile growth-rate regimes for
  beta_s<1. It should not be called empirical PIC data.

| Pages | Main content and locators |
|---|---|
| 1-2 | Abstract/introduction, radiation and charge-starvation scope; magnetization and inertial scale; Eqs.(1)-(6) |
| 3 | Alfvénic scalings, Harris versus localized profile index n, tearing/charge-starvation scales; Eqs.(7)-(16) |
| 4 | Scale comparison, tearing-range spectra and qualitative charge-starved cascade; Eqs.(17)-(26) |
| 5 | Conclusions and caveats; Eqs.(27)-(33); acknowledgments; Appendix (A1)-(A2) |
| 6 | Inner ODE, matching condition and asymptotic Regions I/II; (A3)-(A12) |
| 7 | Figure 1; matching constants and tearing growth; (A13)-(A21) |
| 8 | Small-beta crossover, twiddle estimates and Figure 2; (A22)-(A30) |
| 9 | Hypergeometric solution and asymptotic matching; (A31)-(A42) |
| 10 | Formal large-beta growth-rate matching, ORCIDs, references; (A43)-(A45) |
| 11 | Remaining references |

The machine-text OCR/extraction can corrupt inequalities: for example,
Appendix A.3's title is **beta_s much less than 1**, not beta_s=1. The
formal large-beta limit is Appendix A.5. The matching function Y and the
hypergeometric function with its own alpha/beta/gamma parameters must not
be conflated with the physical pressure parameter beta_s. Footnote 5 on
p.9 explicitly warns of the beta distinction.

There are 33 numbered main equations and 45 numbered appendix equations.
`supplied-math-label-anchors.json` records all 78 tag locations, columns
and nearby PDF-text contexts. These contexts are **not isolated equation
transcriptions or authoritative TeX**; long displays can exceed their
context boxes, and math glyph ordering is unreliable. Use the actual
page renders for mathematical signs, fractions and grouping.

Crossref carries four publisher-deposited MathML spans in its abstract.
They are preserved in `crossref-abstract-math-spans.json`, explicitly
limited to the abstract. After human clearance, all 149 publisher
math/tex script nodes, including all 78 numbered displays, were obtained.
Those exact source strings and the independently checked page locators
supersede the earlier inability to obtain full-article machine mathematics.
No author-source archive is claimed.

## Data, programs and availability boundary

The complete supplied PDF has no identified explicit Data Availability
section and no embedded target-linked program or dataset/deposit URI.
Its 157 distinct embedded URI annotations are inventoried in
`supplied-link-inventory.json`; the arXiv URI noted above is a cited
different paper. The paper provides the governing inner ODE, asymptotic
formulas and Figure 1's three dimensionless parameters, but no original
solver program or raw curve arrays were obtained in this preflight.

This does not prove that no public code/data record exists or that the
source authors could not supply one. It also does not assert that a
full PIC dataset is missing from an article that reports no new PIC
calculation. Data/supplementary prose on the now-accessible publisher
page remains unassessed by this reviewer pending a main-text capture;
the access block itself has been resolved.

## Saved extraction and evidence

`supplied-page-01.txt` through `supplied-page-11.txt` retain the PDF layout
text; corresponding `*-compact.txt` files and
`supplied-full-text-compact.txt` supply readable ordered text. Source
math must still be checked against the page images. Extraction used the
bundled pypdf/pdfplumber tools; PDF rendering used Poppler. The detailed
`source-editions-preflight.json` binds all relevant hashes, software
versions, dates, page/figure/equation inventories and reading scope.

Only local scratch evidence was written. No manuscript/PDF was authored,
no publisher metadata changed, no paper submitted, no source author
contacted, no browser challenge bypassed and no Git mutation performed.
