---
title: "Reflect & Review: draft 002 (brainstorm, no word limit)"
type: analysis
status: brainstorm
created: 2026-11-23
updated: 2026-11-24
revision_contributor: ChatGPT (XYZ framework, external research, consulting brainstorm)
authors: Albert Gruning (opinions, framing), Claude Opus 5.5 (research, fact-check, structure)
assignment: "[[sources/week-4-08-reflect-and-review]]"
chosen_paper: "Zhang et al., Nature 551, 601–604 (2017)"
---

# Reflect & Review: draft 002

> **What this is.** A long brainstorm for the official Week 3 *Reflect & Review* activity ([source note](../sources/week-4-08-reflect-and-review.md)). There's no length limit here; the eDX box itself takes **150–300 words**, so a condensed version gets cut from this later. It builds on PAPER-DRAFT-001 (Grok, private Google Doc) and on the wiki: [[concepts/quantum-simulation]], [[concepts/quantum-annealing]], [[concepts/vqe]], [[concepts/quantum-chemistry]], [[concepts/photon-polarization-qubits]].
>
> **Tags used below:** **[fact]** = checked against a linked source on 2026-11-23 · **[opinion]** = Albert's position · **[reasoning]** = Claude's argument · **[to verify]** = not checked yet, don't publish as fact.

---


## 0A. XYZ Impact Model — Albert's framework (2026-11-24)

**[opinion / proposed analytical framework]** Evaluate research as a time-dependent vector I(t) = (X(t), Y(t), Z(t)), not a single popularity ranking.

| Axis | Meaning | Evidence to collect |
|---|---|---|
| X — scientific | New physics, technical capability, reproducibility, subsequent research | Peer-reviewed results, independent replications, normalized citations, credible classical baselines |
| Y — media | Visibility, framing, institutional reputation and expectations | Dated headlines, outlet categories, article counts, prominence, audience reach and sentiment |
| Z — business / financial / fintech | Capital allocation and actual economic activity | Grants, equity financing, contracts, recognized revenue, deployments, hiring, customer outcomes and financial-sector applications |

Time is a parameter, not another score. The axes are conceptually distinct, not assumed statistically independent. Capital raised, revenue, valuation and realized client value are different measures; report them separately. Compare the 2016–17 launch windows and 2026 follow-up; distinguish paper-level evidence from platform-level proxies. Numerical hypotheses are now permitted, but label subjective scores separately from measured indices. Calibrate X=1 against [Attention Is All You Need](https://arxiv.org/abs/1706.03762), Y=1 against [AlphaZero](https://arxiv.org/abs/1712.01815), and Z=1 against the [DeepSeek V3](https://arxiv.org/abs/2412.19437) / [R1](https://arxiv.org/abs/2501.12948) disruption event. Reference values are chosen anchors, not ceilings. Illustrative Zhang vector (0.35,0.15,0.10) is a hypothesis, not data. Measure citations/adoption at matched ages, press reach within matched windows, and attributable cost reductions/commercial adoption separately. DeepSeek V3 efficiency involves MoE, precision and co-design, not just R1 distillation; $5.576M reported training compute is not total development cost. The quantum analogy is a cost or capability discontinuity on equivalent tasks. [Google Sycamore 2019](https://research.google/pubs/quantum-supremacy-using-a-programmable-superconducting-processor/) claimed 200 seconds vs 10,000 years; [IBM counterestimate](https://www.ibm.com/quantum/blog/on-quantum-supremacy) 2.5 days; [Willow 2024](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/) advances error correction and sampling. These are task-specific, not commercial advantage. Classical baselines keep evolving.

| Contribution | X: scientific | Y: media | Z: business |
|---|---|---|---|
| Zhang (2017) | 53-ion analog many-body dynamics and domain correlations | Shared 50+ headline with Bernien; IBM prototype announced earlier | Platform credibility, not documented immediate revenue |
| O'Malley (2016) | H₂ molecular energies; VQE vs phase estimation | Accessible chemistry narrative; comparative reach not measured | Chemistry proof of concept, not industrial production |
| Kandala (2017) | Hardware-efficient VQE, up to BeH₂, quantum magnet | IBM ecosystem and chemistry narrative | Enterprise research pathway, not proven profitable chemistry |
| Trapped-ion ecosystem (2026) | Helios, digital magnetism and QEC experiments | Commercial firms generate their own headlines | IPO, contracts, deployments; attribution to Zhang alone not established |

**Working thesis:** the chosen paper may score differently on each axis. The press competition is documented, but relative reach and causal impact need a media corpus. Commercial trapped-ion activity supports the relevance of the underlying technology, not a claim that Zhang caused all subsequent investment. Scientific impact can precede commercial relevance by years; headlines can precede both.

### Bloch-inspired representation (user proposal)

Reuse Bloch/Poincaré sphere geometry as a visualization, not quantum-state physics: raw I=(X,Y,Z), r=||I||₂, unit direction I/r for r>0. Benchmarks independently equal 1; raw coordinates may exceed 1 and r may exceed 1 even when every coordinate is below 1. Distinguish axis overflow from radial overflow; retain magnitude and original coordinates when normalizing. Zero vector has no direction. No quantum density matrix or probability interpretation. OOP design: reusable sphere renderer with domain-specific axis labels, raw/unit modes, overflow indicator and time trajectories. See [[analyses/qimono-live-delivery]] for operationalization.

## 0B. Hardware race: 2017 versus November 2026

**[external evidence, checked 2026-11-24]** IBM uses superconducting circuit qubits (artificial atoms controlled by electrical/microwave signals at cryogenic temperatures). Zhang used trapped ytterbium ions. The other two assigned papers used superconducting hardware. Bernien's neutral Rydberg atoms are a third modality.

| Date / system | Scale | Quality / architecture | Status |
|---|---|---|---|
| IBM, 10 Nov 2017 | 20-qubit client system; 50-qubit prototype | Superconducting; average coherence 90 microseconds for 20-qubit system, similar metrics for prototype | Operational prototype; client access to 20 planned by year end |
| Zhang, 29–30 Nov 2017 | 53 ions | Long-range Ising analog simulator; individual readout around 99% | Published experiment, not universal 53-qubit gate machine |
| Bernien, same Nature issue | 51 neutral atoms | Rydberg interactions, analog simulation | Independent experiment |
| IBM Nighthawk r2, 31 Aug 2026 | 120 programmable qubits; 218 couplers and 120 reset elements (458 physical quantum elements total) | Accurate observable estimation with 7,500+ gates; >100,000 circuits/s, up to 25× Heron throughput; independent fast reset; median idle T1 about 200 microseconds | Available on IBM Quantum Platform |
| IBM Nighthawk r3, announced 11 Nov 2026 | 520 programmable qubits | Target 10,000 quantum operations | Next generation, not established as deployed; two linked r3s / 1,040 programmable qubits planned for 2027 |
| IBM Starling / Blue Jay | Roadmap | Fault-tolerant targets for 2029 / 2033+ | Targets, not delivered systems |
| Quantinuum Helios, Nature June 2026 | 98 physical barium-ion qubits | QCCD shuttling, all-to-all; average 1Q fidelity 99.9975%, 2Q 99.921%, SPAM 99.952% (from reported infidelities) | Commercial system and peer-reviewed benchmark |
| Quantinuum, Oct 2026 | Helios logical-memory experiment | Company reports 99.9995% logical memory fidelity per operation in specific QEC experiment | Not universal logical-gate fidelity or million-gate algorithm guarantee |
| IonQ Superion 256, Sept 2026 | 256-qubit platform announced | Electronic Qubit Control; company cites 99.99% 2Q record from 2025, not a demonstrated fleet-wide Superion figure | Announced platform; November report cites demand and planned NVIDIA deployment |

Sources: [IBM 2017 original release](https://www.prnewswire.com/news-releases/ibm-announces-advances-to-ibm-quantum-systems--ecosystem-300553715.html); [IBM r2](https://www.ibm.com/quantum/blog/nighthawk-r2); [IBM QDC 2026](https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027); [IBM roadmap](https://www.ibm.com/roadmaps/quantum); [Helios Nature paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13322971/), [preprint](https://arxiv.org/abs/2511.05465); [Quantinuum logical memory](https://www.quantinuum.com/blog/quantinuum-closes-in-on-one-million-error-free-operations); [IonQ Superion](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing); [IonQ Q3](https://investors.ionq.com/news/news-details/2026/IonQ-Announces-Record-3Q26-Revenues-and-Raises-FY2026-Guidance-to-505---515-Million-as-Backlog-Grows-to-1-2-Billion/).

**Reliability is not qubit count.** Compare physical and logical qubits separately; report 1Q/2Q error, SPAM, T1/T2, connectivity, gate duration, circuit depth, throughput, QEC overhead and application-level error. IBM's 7,500-gate observable result is not a fidelity percentage, and Zhang's readout fidelity is not a two-qubit gate benchmark. Trapped ions generally offer strong connectivity/coherence at the cost of slower operations and demanding control/shuttling; superconducting chips offer fast gates and fabrication integration but require cryogenics and routing on restricted connectivity. The 2017 headline contest (50 vs 51 vs 53) compared unlike capabilities. The 2026 comparison must not repeat that mistake.

## 0C. Chemistry, nitrogenase and food production: the industrial bridge

**[course]** [[concepts/quantum-chemistry#^haber-bosch-nitrogenase]] and [Chuang's chemistry lesson](../sources/week-4-04-simulation-of-chemistry-problems.md), raw week4 transcript approximately 2:52–4:31, compare industrial Haber–Bosch (about 450 °C, around 200 atm in the corrected Learn note) with bacterial nitrogenase operating under mild conditions. The aim is to understand alternative reaction pathways, not merely to raise temperature. The example concerns ammonia/fertilizer production, not quantum computers manufacturing enzymes.

**[background]** N₂ + 3H₂ → 2NH₃. Nitrogenase uses an iron-molybdenum cofactor (FeMoco) and electron/proton transfer coupled to ATP consumption; biological fixation is not energy-free. The electronic structure is challenging because several metal centers have strongly correlated electrons and competing spin states. This bridges Zhang's many-body magnetism and the molecular-energy papers: correlated quantum systems are a common scientific theme, but the Ising experiment does not itself solve nitrogenase.

**[external evidence]** The [IEA Ammonia Technology Roadmap](https://www.iea.org/reports/ammonia-technology-roadmap) estimates about 70% of ammonia goes to fertilizer; ammonia production represents about 2% of global final energy use and 1.3% of energy-system CO₂ emissions. This gives an industrial KPI, not a forecast of quantum savings. [Pivot Bio's 2021 Series D](https://www.pivotbio.com/press-releases/series-d) raised $430M for microbial nitrogen innovation (not quantum computing): evidence of economic demand for alternative nitrogen pathways. A [2026 ACS presentation](https://acs.digitellinc.com/p/s/design-of-an-artificial-nitrogenase-that-reduces-dinitrogen-to-ammonia-648930) reports a designed artificial protein binding native FeMoco and reducing nitrogen to ammonia; conference report, not commercial scale or quantum involvement.

**Classical challenge:** [Zhai et al., arXiv:2601.04621](https://arxiv.org/abs/2601.04621), revised June 2026, reports classical chemical-accuracy results for a FeMo-cofactor model. [Reproducibility data](https://zenodo.org/records/22116121). A model result does not solve the complete enzyme, catalytic cycle, kinetics, solvent, ATP supply or plant economics. Quantum research must outperform the strongest contemporary classical method on a specified task.

**Candidate industrial research program [proposal]:** select an active-space Hamiltonian for a catalyst fragment with a chemistry partner; benchmark classical DFT, coupled cluster where appropriate, DMRG and exact diagonalization for small cases; compare VQE or future phase estimation for energy differences and uncertainty. Expand only after credible accuracy/time/cost improvement. Chemistry validation includes reaction barriers, selectivity, turnover, stability, feedstock, bioreactor scale and lifecycle emissions. Target business measures: cost per tonne NH₃, kWh per tonne, CO₂e per tonne, nitrogen-use efficiency and crop yield. A reduction in computation cost is not automatically a reduction in fertilizer cost.

Illustrative economics (not a forecast): a 1 million tonne/year plant saving $10 per tonne would save $10M/year before implementation costs; whether a quantum-derived catalyst can deliver that is open. Green hydrogen, conventional catalyst improvements and microbial engineering remain competing approaches. The chemistry papers deserve serious Z-axis attention even though Zhang is selected.

## 0D. Investment as a corporate external consultant, not a stock tip

**[Albert's position]** Yes, 100% in favor of funding further investigation of the chosen direction. That is conviction in staged R&D, not allocating 100% of capital to one vendor. My earlier ML consulting work identified which business problems suited forecasting, sentiment analysis or another ML method. The same discovery practice applies to quantum: start from the client's problem, not a fashionable algorithm.

### Capital and customer evidence (USD; distinguish transaction types)

| Example | Amount / evidence | Interpretation |
|---|---|---|
| IBM, June 2026 | >$10B planned investment over five years | Corporate spending commitment, not annual revenue or a grant to Zhang |
| Quantinuum, June 2026 | 28M shares × $60 = $1.68B gross IPO base proceeds, before fees | Capital raise, not operating revenue |
| IonQ / Oxford Ionics, 2025 | $1.1B acquisition, reported by McKinsey | Technology consolidation, not project budget |
| IonQ Q3 2026 | $505–515M FY revenue guidance, $1.2B reported backlog | Guidance and backlog, not cash collected; diversified company |
| Quantum technology sector, 2025 | $12.6B startup investment, 6.3× 2024 (McKinsey 2026) | Sector-wide financing, not just trapped ions |
| Pivot Bio, 2021 | $430M Series D | Adjacent agriculture opportunity, no quantum claim |

Sources: [IBM commitment](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing%2C-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers); [Quantinuum IPO](https://www.quantinuum.com/press-releases/quantinuum-announces-pricing-of-upsized-initial-public-offering); [IonQ results](https://investors.ionq.com/news/news-details/2026/IonQ-Announces-Record-3Q26-Revenues-and-Raises-FY2026-Guidance-to-505---515-Million-as-Backlog-Grows-to-1-2-Billion/); [McKinsey monitor](https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/mckinsey-quantum-technology-monitor-2026-a-commercial-tipping-point); [MIT Quantum Index funding](https://qir.mit.edu/funding/) provides alternative definitions and examples: Quantinuum $600M Series B, QuEra $230M Series B, PsiQuantum $1B Series E, IQM $300M Series B, Quantum Machines $170M Series C. Do not add these deals to aggregate funding without checking overlap.

**Competition for clients:** IonQ and Quantinuum compete in overlapping enterprise, government and research markets, with different trapped-ion architectures and offerings. IonQ cites Tempo deployments and future Superion demand; Quantinuum has Helios and [JPMorgan/Argonne QAOA research](https://www.jpmorganchase.com/about/technology/news/jpmorganchase-research-collaboration-shows-quantum-algorithm-speedup). The latter is a theoretical algorithmic speedup, not profitable portfolio optimization. [Quantinuum SEC Q3 filing](https://www.sec.gov/Archives/edgar/data/2110105/000162828026072454/qnt-20260930.htm) documents ongoing scaling R&D. The [OQC/JPMorgan/AMD 2026 collaboration](https://www.jpmorganchase.com/about/technology/blog/oqc-jpmc-amd-quantum-ai-platform) shows fintech clients also evaluating superconducting platforms. No specific head-to-head tender established.

**Employment:** Albert personally explored Rigetti vacancies during his job search. [Rigetti's careers board](https://www.rigetti.com/careers) and [current listings](https://jobs.lever.co/rigetti?p=careers) include lead quantum systems-performance engineer. A dated snapshot verifies active hiring, not an increasing trend unless historical vacancy counts are collected with the same method. [Rigetti Q3 2026 results](https://investors.rigetti.com/news-releases/news-release-details/rigetti-computing-reports-third-quarter-2026-financial-results) are a separate commercial indicator. Hiring, funding and revenue indicate ecosystem development, not proof of quantum advantage.

### Concrete funding decision [illustrative proposal, not a quote or existing budget]

As an external consultant to a fertilizer/materials company or funding agency, propose a $250,000 six-month capped R&D pilot:

| Work package | USD | Exit criterion |
|---|---:|---|
| Discovery and domain expert workshops | 25,000 | Defined KPI, dataset and decision owner |
| Classical baseline and Hamiltonian/optimization formulation | 60,000 | Reproducible reference and tolerance |
| Vendor-neutral feasibility and cloud runs | 60,000 | Comparable IBM and trapped-ion experiments; cost and error logged |
| Chemistry/materials expert validation | 45,000 | Meaningful error bars and validation plan |
| Security readiness and integration | 25,000 | Crypto inventory, migration priorities, reproducible integration |
| Contingency and independent review | 35,000 | Go/no-go report |
| **Total** | **250,000** | **No scale-up without evidence** |

First release $85k for discovery and classical baseline; release remaining $165k only if a credible quantum hypothesis and feasible resources exist. A later $1M follow-on is a separate decision subject to independent review, client cofunding and risk limits. For an agency funding the original research direction, reserve a distinct basic-science track for replication, scalable ion control and error correction; commercial ROI need not be immediate. These are proposed planning assumptions, not promised returns.

### Qimono service concept: We help you find your quantum advantage

**[proposed offering, not a claim of existing paid clients or delivered advantage]** IBM's [Quantum Working Groups](https://www.ibm.com/quantum/blog/quantum-working-groups) unite researchers and domain experts in healthcare, materials, high-energy physics, optimization and sustainability. Its [quantum readiness training](https://quantum.cloud.ibm.com/learning/en/courses/quantum-business-foundations/how-to-become-quantum-ready) frames strategic use-case discovery; [QDC 2026](https://www.ibm.com/quantum/blog/qdc-2026) describes client workflows, benchmarking and ecosystem tools. This is a precedent, not an affiliation or a claim of equivalent capabilities.

| Service | Concrete deliverable | Baseline / success test |
|---|---|---|
| Quantum Advantage Discovery | 2–3 week workshop, ranked use-case register, resource estimates, vendor-neutral roadmap | Business value, bottleneck, realistic resources; no-go acceptable |
| Optimization & heuristics | Scheduling/routing/portfolio constraints, QUBO/Ising mapping where suitable; classical and quantum-inspired/quantum experiments | MILP, CP-SAT, strong heuristics; quality, runtime, feasibility, cost |
| Quantum Security Readiness | Crypto inventory, data retention/harvest-now-decrypt-later exposure, crypto-agility and PQC migration checklist | NIST standards, interoperability, risk ownership; no QPU needed |
| Quantum Leap: ML → QML | Audit AI/RAG/ML pipelines; select a narrow feature-map, kernel or variational-model hypothesis | Held-out predictive metrics, classical kernels/NNs, encoding, latency and cost; RAG remains classical unless evidence supports a specific change |

For fintech, near-term risk management may be more concrete than computing advantage: [Reuters, 19 Nov 2026](https://www.reuters.com/legal/government/global-securities-watchdog-urges-immediate-action-quantum-risks-finance-2026-11-19/) reports IOSCO urging immediate quantum-risk preparation. Separate PQC (classical algorithms resistant to known quantum attacks) from QKD and speculative QML. See [[concepts/post-quantum-cryptography]], [[concepts/quantum-annealing]], [[concepts/vqe]], [[concepts/quantum-simulation]]. First demonstrations can use Qimono's educational experiments, not production claims. Illustrative discovery engagement $10–25k, scoped prototype $40–100k; actual pricing depends on expertise, compute and scope.

**Candidate first-person reflection [draft]:** As an external technology consultant, I would fund this research direction because its scientific evidence and subsequent development of the trapped-ion ecosystem justify measured exploration of industrial opportunities. I would not buy hardware on the basis of a qubit-count headline. I would first identify a valuable computational bottleneck, establish the strongest classical baseline, and allocate a limited budget to independent benchmarks. This is how I approached machine-learning use cases in the past, and how I would position Qimono in the quantum era: helping companies discover whether and where quantum computing might produce a defensible advantage, while preparing them for quantum-security risks today.

**LinkedIn positioning brainstorm (not published):**

> At Qimono, we are developing a vendor-neutral quantum readiness and opportunity-assessment practice. We help businesses explore where quantum computing could create measurable value: optimization and advanced heuristics, quantum security readiness, and our Quantum Leap pathway for teams already using AI, RAG and machine learning. We start with your business problem, benchmark against classical methods, and recommend quantum only where the evidence supports it. No quantum washing. Just better questions, reproducible experiments and a roadmap to measurable results.

For the final reflection, focus on the funding decision and evidence rather than advertising. Keep the longer commercial concept here as a separate brainstorm.

---

## 0. The three assigned papers, one line each

| # | Paper | Platform · institution | One-line takeaway |
|---|---|---|---|
| 1 | [[papers/zhang-2017-53-ion-dynamical-phase-transition\|Zhang et al. 2017]], *Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator*, **Nature 551, 601–604 (30 Nov 2017)**. [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf\|📄 local PDF]] | 53 trapped ¹⁷¹Yb⁺ ions · JQI (University of Maryland + NIST), Monroe also IonQ | Analog simulation of a long-range transverse-field Ising model. Individual readout of every ion (~99%) lets them measure many-body correlations shot by shot, and they see a *dynamical* phase transition. **← chosen** |
| 2 | [[papers/omalley-2016-h2-molecular-energies\|O'Malley et al. 2016]], *Scalable quantum simulation of molecular energies*, **Phys. Rev. X 6, 031007 (2016)**. [[mit-raw/external/papers/omalley-2016-h2-molecular-energies-arxiv-1512.06860.pdf\|📄 local PDF]] | Superconducting · Google + UCSB (+ Harvard, LBNL, Tufts, UCL) | H₂ energy curve via VQE (chemical accuracy) and Trotterized phase estimation. VQE is more robust to errors. |
| 3 | [[papers/kandala-2017-hardware-efficient-vqe\|Kandala et al. 2017]], *Hardware-efficient VQE for small molecules and quantum magnets*, **Nature 549, 242–246 (14 Sep 2017)**. [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf\|📄 local PDF]] | Superconducting · IBM T.J. Watson | Up to 6 qubits, 100+ Pauli terms, molecules up to BeH₂, plus a quantum magnet. Results match a noisy device model. |

Paper notes (page-by-page guides with wiki links): [[papers/zhang-2017-53-ion-dynamical-phase-transition]] · [[papers/omalley-2016-h2-molecular-energies]] · [[papers/kandala-2017-hardware-efficient-vqe]] · Combined summary: [external note](/mit-raw/external/reflect-review-papers.md).

---

## Q1. Impact on a business industry: was it the most influential of the three?

### Albert's thesis
**Hypothesis: not the dominant press story, partly because of timing rather than quality.** See XYZ framework above; comparative coverage is not quantified. The press was busy with other stories, and quantum computing has a bad-press problem: hype, then backlash. **[opinion]**

### Evidence: the timing was brutal **[fact]**

1. **It shared the Nature issue with a rival record.** The same issue (Nature 551, 30 Nov 2017) carried Lukin's group (Harvard/MIT) with a **51-atom Rydberg simulator**. Physics World covered "two independent research groups" in one story ([Physics World, 29 Nov 2017](https://physicsworld.com/a/quantum-simulators-shed-new-light-on-magnetic-phase-transitions/)). Even UMD's own press release announced "two independent teams" with "more than 50" qubits ([UMD CMNS](https://cmns.umd.edu/news-events/news/quantum-simulators-wield-control-over-more-50-qubits-setting-new-record)). The headline was "50+ qubits", shared between two labs, not "53 ions".
2. **IBM had taken the "50-qubit" mainstream headline three weeks earlier.** On **10 Nov 2017** IBM announced a **50-qubit prototype** and a 20-qubit system on its cloud ([MIT Technology Review](https://www.technologyreview.com/2017/11/10/147728/ibm-raises-the-bar-with-a-50-qubit-quantum-computer/), [AP via Phys.org](https://phys.org/pdf429532312.pdf), [Science News](https://www.sciencenews.org/article/quantum-computing-steps-forward-50-qubit-prototype)). Bloomberg framed it as IBM vs Google in the race to "quantum supremacy" ([DataCenterKnowledge/Bloomberg](https://datacenterknowledge.com/supercomputers/ibm-ups-pressure-on-rivals-with-quantum-computer-prototype)). By 30 Nov IBM had established a competing 50-qubit headline; public perception has not been measured.
3. **Examples of coverage include specialist outlets.** A comprehensive media search is still needed. The 53-ion result went to Physics World, IEEE Spectrum, HPCwire, Optica OPN and Nature Asia, the specialist science press ([IEEE Spectrum](https://spectrum.ieee.org/quantum-simulators-get-bigger-and-badder), [HPCwire](https://www.hpcwire.com/2017/11/29/two-quantum-simulators-cross-50-qubit-threshold/), [Optica OPN](https://www.optica-opn.org/home/newsroom/2017/december/quantum_simulators_leap_ahead)). The IBM announcement went through AP and Bloomberg to the business press.
4. **Even friendly coverage carried a disclaimer.** Physics World quoted Christine Muschik (Waterloo) calling these simulators "textbook examples of not being quantum computers", because they don't encode a complete gate set ([Physics World](https://physicsworld.com/a/quantum-simulators-shed-new-light-on-magnetic-phase-transitions/)). For a business reader that line reads as "not a product".
5. **Background [to verify before publishing]:** late 2017 was also the Bitcoin mania (peaking around mid-December 2017) and the AlphaGo Zero moment for AI (Nature, October 2017). Competing "future of computing" stories crowded the same news cycle.

### Evidence: quantum computing's bad-press cycle **[fact]**
- **Hype, then crash.** In January 2025 one sentence from Nvidia's Jensen Huang ("15 years… early side, 30… late side") sent IonQ, Rigetti and D-Wave down roughly 30–45% in a day ([Fortune](https://fortune.com/2025/01/09/nvidia-ceo-jensen-huang-tanks-quantum-computing-stocks/), [CNBC via NBC](https://nbcmiami.com/news/business/money-report/quantum-stocks-like-rigetti-plunge-after-nvidias-huang-says-the-computers-are-15-to-30-years-away/3509856)). One analyst's read: "any dollar chasing quantum computing stocks is not chasing AI stocks" ([Reuters via Cyprus Mail](https://cyprus-mail.com/2025/01/11/quantum-computing-stocks-take-a-hit-as-nvidia-ceo-predicts-long-road-ahead)). The press frames quantum *against* AI.
- **"Always five years away."** In August 2026 the cryptography mailing list was still circulating an essay titled "Why full-fledged quantum computers might always be five years away" ([metzdowd cryptography list](https://www.metzdowd.com/pipermail/cryptography/2026-August/039724.html)).
- **Even the best coverage gets corrected.** The Economist's 29 July 2026 feature, *"Quantum computers promise mathematical superpowers"*, was called "by a clear margin, the best quantum computing article I have seen", yet still "wrong" on several points by a practitioner reviewer ([PostQuantum review](https://postquantum.com/industry-news/economist-quantum-article-review/)).
- **Claims get withdrawn.** At IBM's own QDC 2026, Jay Gambetta's keynote described "classical researchers overtaking quantum results, claims being withdrawn as classical makes improvements" ([SiliconANGLE, 12 Nov 2026](https://siliconangle.com/?p=854010)). The field now says this openly.

### So what was its real business impact? **[reasoning]**
- **Industry: materials and magnetism, plus the trapped-ion hardware industry itself.** [[papers/zhang-2017-53-ion-dynamical-phase-transition|Zhang's paper]] simulated a quantum magnet, the model family behind magnetic materials and the same Ising Hamiltonian that [[concepts/quantum-annealing]] uses to encode optimization problems. Its direct business effect wasn't a product. It was **credibility capital** for trapped ions as a scalable, individually controllable platform.
- **The line from 2017 to 2026 is visible in Nature:**
  - 2026: *Digital quantum magnetism on a trapped-ion quantum computer* (Haghshenas et al., **Nature**, doi:10.1038/s41586-026-10445-3), Quantinuum hardware with TUM theory, "a regime in which classical computational methods begin to fail" ([TUM/MCQST](https://www.mcqst.de/news-and-events/news/quantum-computer-opens-a-new-path-to-practical-scientific-applications.html)). **[fact]** That's Zhang's question (quantum magnetism with ions) asked again with a *digital*, gate-based machine.
  - June 2026: Quantinuum's **98-qubit Helios**, "all-to-all connectivity", published in **Nature** ([Nature Asia summary](https://www.natureasia.com/ja-jp/phys-sci/research/15569), doi:10.1038/s41586-026-10676-4). **[fact]** All-to-all connectivity is exactly the property Zhang highlighted (long-range interactions, high connectivity).
  - Monroe, now at Duke, is still doing many-body simulations on ions, such as "string breaking" in particle physics using domain walls, a direct echo of the 2017 domain statistics ([Physics World](https://physicsworld.com/?p=130926)). **[fact]**
- **Was it the most influential of the three?** In the **press, no** (timing, a shared headline, "not a computer"). In **science and industry, arguably yes over the long run**: the chemistry-VQE line (papers 2 and 3) became an algorithm family everyone uses, but its "chemistry advantage" story keeps hitting classical counterattacks. For example, a January 2026 preprint claims a **classical solution of the FeMo-cofactor model to chemical accuracy** (Zhai et al., arXiv:2601.04621, discussed on *The New Quantum Era* podcast) ([Apple Podcasts show notes](https://podcasts.apple.com/us/podcast/the-new-quantum-era---innovation-in-quantum-computing,-science-and-technology/id1637676725)). **[fact, show-notes level; read the preprint before citing]** FeMoco is the nitrogenase cofactor, the same enzyme behind Chuang's Haber–Bosch example in our Week 3 chemistry lecture ([[concepts/quantum-chemistry]]). Meanwhile, the ion line kept growing into gate-model machines.

> **Candidate thesis sentence [opinion + reasoning]:** "Zhang et al. lost the 2017 press cycle (it shared a Nature issue with a 51-atom rival, three weeks after IBM's 50-qubit headline, and was labelled 'not a quantum computer'), but it won the decade: its signature properties, individual control and all-to-all connectivity, are the selling points of 2026's trapped-ion machines in Nature."


> [!note]- 🔗 Wiki connections for Q1
> - **What the paper actually measured:** single-shot readout of all 53 ions ([[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=3|Fig. 3, p.3]]) and spin domains as many-body correlators ([[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf#page=4|Fig. 4, p.4]]). This is Chuang's issue #3, "what to measure?": [[concepts/quantum-simulation#^ideas-and-issues]].
> - **Analog vs digital simulation:** [[concepts/quantum-simulation#^approaches]] and [[concepts/quantum-simulation#^analog-deformation]]. The 2026 Nature "digital quantum magnetism" paper is the *digital* answer to Zhang's *analog* question.
> - **Why "hard to compute classically" holds:** DMRG-type methods excel in 1D with short-range entanglement ([[concepts/quantum-simulation#^quantum-inspired]], [[papers/zhang-2017-53-ion-dynamical-phase-transition]]); Zhang's couplings are long-range.
> - **The chemistry side of the comparison:** the FeMoco/nitrogenase example is Chuang's Haber–Bosch story: [[concepts/quantum-chemistry#^haber-bosch-nitrogenase]], [[concepts/quantum-chemistry#^two-pathways]].
> - **"Claims withdrawn as classical improves"** matches the course's own caution on annealing: [[concepts/quantum-annealing#^no-enhancement-evidence]] and the D-Wave story [[concepts/quantum-annealing#^dwave]].
> - **Graded questions on the same material:** [[quizzes/week-3#Q2: Ideas and Issues of Quantum Simulation]], [[quizzes/week-3#Q1: Quantum-Inspired Approximations]], [[quizzes/week-3#Q1: Ultra-Cold Atoms]].

---

## Q2. Corporate superconducting vs university atoms: did the institution change expectations?

### What the question is really asking (plain version)
Two papers came from **big companies** (Google, IBM) using **superconducting chips**; one came from a **university and government lab** (UMD/NIST) using **atoms**. The course wants you to compare **how the news treated them**, and whether that **shaped what people expected next**: who would build "the" quantum computer, how soon, and what for. It's a question about *perception and narrative*, not physics.

### Candidate answer **[reasoning, with facts]**
- **Corporate results arrived wrapped in a product story.** IBM's late-2017 news came with a cloud offering ("20-qubit system available through its cloud") and a race narrative against Google ([MIT Tech Review](https://www.technologyreview.com/2017/11/10/147728/ibm-raises-the-bar-with-a-50-qubit-quantum-computer/), [Bloomberg](https://datacenterknowledge.com/supercomputers/ibm-ups-pressure-on-rivals-with-quantum-computer-prototype)). The chemistry papers (H₂, BeH₂) were easy to translate into "drugs and materials". **Expectation created: near-term, commercial, a race between tech giants.**
- **The university result arrived wrapped in a science story:** "magnetic phase transitions", "simulators, not computers" ([Physics World](https://physicsworld.com/a/quantum-simulators-shed-new-light-on-magnetic-phase-transitions/)). **Expectation created: important physics, a long road to a computer.**
- **The twist [fact + reasoning]:** the university press release itself was built to bridge that gap. It named Monroe as "co-founder and chief scientist at the startup IonQ" and called his simulator "part of a blueprint for a general-purpose quantum computer" ([UMD CMNS](https://cmns.umd.edu/index.php/news-events/news/quantum-simulators-wield-control-over-more-50-qubits-setting-new-record)). Even in 2017, the university line had a company attached.
- **Nine years later [fact]:** the "university technology" is public-market technology. IonQ trades on the NYSE (IONQ), and Quantinuum (trapped ions, majority-owned by Honeywell) had a 2026 IPO that raised **$1.68B at a >$15B valuation** ([Motley Fool, 16 Jun 2026](https://www.fool.com/investing/2026/06/16/quantinuums-ipo-is-putting-pressure-on-ionq-rigett/)). Commentators now frame IonQ and Quantinuum as "fighting on the same battlefield" for enterprise and government contracts (same source).
- **Lesson [opinion]:** institution and technology shaped the *first* expectation (corporate = product, university = physics), but the *outcome* didn't respect that split. The press measured **who announced**; the market later rewarded **what scaled**.

> **Candidate paragraph:** "In 2017 the corporate superconducting papers were reported as a product race (cloud access, IBM vs Google, 'quantum supremacy'), while the university trapped-ion result was reported as physics, even 'not a quantum computer'. That framing set expectations: companies would deliver, universities would discover. Nine years on, trapped ions are themselves a public-market industry (IonQ on the NYSE, Quantinuum's 2026 IPO). The press measured who announced; the market rewarded what scaled."


> [!note]- 🔗 Wiki connections for Q2
> - **The two hardware worlds in our notes:** atoms and ions (analog simulators, BECs, time-averaged Hamiltonians) in [[concepts/quantum-simulation#^analog-deformation]] and [[quizzes/week-3#Q1: Ultra-Cold Atoms]]; superconducting circuits in IBM's roadmap and our [Qiskit circuits](/tools/circuits/README.md).
> - **A corporate example in our own course:** D-Wave's "adiabatic → annealing" rebranding, told by Shor: [[concepts/quantum-annealing#^dwave]] and [[sources/week-5-03b-quantum-annealing-expert-view]]. Institution shaped expectations there too.
> - **The IBM paper's authors (Chow, Gambetta)** lead IBM's 2026 roadmap: [[papers/kandala-2017-hardware-efficient-vqe]].

---

## Q3. Would I invest in my chosen paper's project? **Yes, 100%** **[opinion]**

### Why **[opinion + reasoning]**
1. **Its properties became the industry's selling points**: individual addressing, high-fidelity readout, all-to-all connectivity. They show up in 2026 Nature papers (Helios, digital quantum magnetism) and in commercial claims.
2. **Simulation is the first honest application.** Feynman's argument, which IBM now repeats as "simulate quantum mechanics… the operating system of the universe" (Gambetta, Think 2026, [IBM Research blog](https://research.ibm.com/blog/ibm-think-2026-modeling-the-universe-with-quantum-computing)). Magnetism and materials come before Shor.
3. **Capital is flowing in this direction.** McKinsey (quoted by The Economist) counted **$12.6bn invested in quantum start-ups in 2025, six times the year before** ([Economist excerpt](https://groups.google.com/g/BZ---/c/XuM0A80czvU)). **[fact via secondary quote; check the Economist original]**

### How I'd allocate it (a funding agency or company mandate) **[opinion]**
*Not financial advice. This is a course reflection: a thought experiment about where research money creates the most value.*

| Bucket | Why | Public examples (exchange: ticker) **[fact: listings as reported 2026]** |
|---|---|---|
| **Trapped-ion line (the chosen paper's descendants)** | Connectivity, fidelity, simulation of magnetism and materials | **IonQ (NYSE: IONQ)**; **Quantinuum (Nasdaq: QNT)**, with **Honeywell** its largest shareholder ([Quantum Zeitgeist](https://quantumzeitgeist.com/public-quantum-computing-companies/), [BrokerChooser](https://brokerchooser.com/news/quantinuums-market-entry-reshapes-competition-for-ionq-rigetti-and-d-wave--89ee9d7e)) |
| **Hedge: superconducting scale-up** | Fabrication and roadmap (see §4) | **IBM (NYSE: IBM)**; Rigetti (Nasdaq: RGTI); Alphabet (Nasdaq: GOOGL) |
| **Hedge: neutral atoms** | Fastest growth in atom count; Lukin's 2017 rival line | **Infleqtion (NYSE: INFQ)**, the first public neutral-atom company, IPO 17 Feb 2026 ([Motley Fool](https://fool.com/investing/2026/05/10/3-quantum-computing-stocks-that-went-public-2026/)) |
| **Different model: annealing (optimization)** | Not gate-model, so a separate thesis (see [[concepts/quantum-annealing]] and the D-Wave expert view) | **D-Wave (NYSE: QBTS)** |
| **Software, education and tools layer** | Every platform needs developers who understand the physics | **Qimono (TM)**: Albert's venture ([qimono.vip](https://www.qimono.vip)). Products: TORCXO, PROXORA (classical vs variational quantum regression), ELSTARU (quantum-learning app). Role: turning results like Zhang's into tools, tutorials and reproducible demos, e.g. this vault's [Qiskit circuits](/tools/circuits/README.md). |

> **Candidate paragraph:** "Yes. I would fund the trapped-ion line this paper helped launch, because its 2017 advantages (individual control, high connectivity, single-shot readout) are exactly what 2026's best ion machines advertise in Nature. As a funding agency I'd hedge across superconducting (IBM) and neutral atoms (Infleqtion), keep annealing (D-Wave) as a separate optimization bet, and reserve a slice for the software and education layer, which is where my own venture, Qimono, works: tools that make results like this reproducible for developers."


> [!note]- 🔗 Wiki connections for Q3
> - **What the money buys, technically:** individual addressing and all-to-all coupling ([[papers/zhang-2017-53-ion-dynamical-phase-transition]]), the same Ising machinery as [[concepts/quantum-annealing#^encoding-and-gap]] and [[concepts/adiabatic-quantum-computing#^ising]].
> - **Why simulation before cryptography:** Shor needs fault tolerance ([[concepts/shors-algorithm#^reduction-summary]]); the risk timeline is in [[concepts/post-quantum-cryptography#^mosca-inequality]].
> - **Qimono's layer, already in this vault:** the [Qiskit circuit generators](/tools/circuits/README.md) (phase estimation, Grover, Shor N = 15, teleportation), the [[analyses/quiz-concept-map]], and this Karpathy-style wiki itself.

---

## 4. Personal insight A (earlier brainstorm; see §0B for verified status distinctions): IBM's "State of the Union" (QDC 2026) vs the 2016–17 papers

> ⚠️ The YouTube link (`pdSBnIghcXk`) couldn't be fetched from this environment, so this section uses press coverage of **IBM Quantum Developer Conference 2026 (11–13 Nov 2026)**. **[to verify]** Watch the video and confirm the quotes.

**What IBM announced [fact]:**
- **Nighthawk r3**: a 520-qubit processor and a **1,040-qubit system in 2027**, replacing an earlier plan to link nine 120-qubit chips ([American Bazaar](https://americanbazaaronline.com/2026/11/12/ibm-expands-quantum-roadmap-with-520-qubit-nighthawk-processor-492207/), [Quantum Computing Report](https://quantumcomputingreport.com/ibm-unveils-520-qubit-nighthawk-r3-processor-1040-qubit-linked-roadmap-and-managed-hybrid-workflows-at-qdc-2026/amp/)).
- **Starling**: fault-tolerant, targeted for **2029**. **Blue Jay**: 2,000 qubits and 1 billion gates, **2033+** ([IBM roadmap](https://ibm.com/roadmaps/quantum)).
- **The "bold 2028":** the 2025 roadmap projected **7,500 two-qubit gates in 2026, 10,000 in 2027, 15,000 by 2028** with long-range couplers ([Converge Digest](https://convergedigest.com/ibm-doubles-quantum-rd-speed-with-300-mm-fab/)).
- **Money:** IBM committed **more than $10B** to its quantum roadmap (June 2026) ([IBM Newsroom](https://newsroom.ibm.com/2026-06-02-ibm-commits-more-than-10-billion-to-quantum-computing,-funding-its-roadmap-from-todays-leading-systems-to-the-worlds-first-fault-tolerant-quantum-computers)).
- **Tone:** at Think 2026, Krishna said quantum advantage is "not 20 years away… not 10 years away… within this year" ([TechTarget](https://www.techtarget.com/searchdatacenter/news/366642895/Quantum-moves-from-promise-to-practice-at-IBM-Think-2026)), and Gambetta: "useful quantum computing is here right now" ([IBM Think 2026](https://www.ibm.com/think/news/live-from-think-2026)).

**Then vs now [reasoning]:**

| | 2016–17 papers | IBM 2026 |
|---|---|---|
| Chemistry | H₂ with 2 effective qubits ([[papers/omalley-2016-h2-molecular-energies|O'Malley]]); BeH₂ with 6 ([[papers/kandala-2017-hardware-efficient-vqe|Kandala]]) | Protein–ligand "quantum-centric" simulations with Cleveland Clinic and RIKEN ([IBM Research](https://research.ibm.com/blog/ibm-think-2026-modeling-the-universe-with-quantum-computing)) |
| Scale | 6 qubits (IBM 2017) | 120 available in 2026 → 520 announced → 1,040 planned for 2027 |
| Claim | "scalable", "hardware-efficient" | "advantage in 2026", "fault-tolerant by 2029" |
| Unchanged | **The VQE loop:** quantum state preparation + **classical** optimization ([[concepts/vqe]]) | still hybrid: "quantum-centric supercomputing" = QPU + HPC |

**Opinion hook [opinion]:** IBM's 2017 paper (Kandala) and IBM's 2026 roadmap share one idea, *hybrid*. What changed is the *size of the promise*. Zhang's group made no promise and shipped a physics result. The investor's job is to discount the promises and price the results.


> [!note]- 🔗 Wiki connections for §4
> - **IBM's own 2017 paper,** for the then-vs-now table: [[papers/kandala-2017-hardware-efficient-vqe]] (6 qubits, BeH₂, [[mit-raw/external/papers/kandala-2017-hardware-efficient-vqe-arxiv-1704.05018.pdf#page=4|Fig. 3, p.4]]).
> - **The hybrid loop IBM still uses:** [[concepts/vqe#^hybrid-loop]], graded in [[quizzes/week-3#Q1: Variational Quantum Eigensolver]].
> - **Gate depth (IBM's 7,500 → 15,000 gates)** matters because deep circuits are where [[concepts/trotterization#^n|Trotter steps]] and [[concepts/phase-estimation#^precision|phase-estimation precision]] get expensive.

---

## 5. Personal insight B: an AI-assisted Riemann Hypothesis proof (claimed 20 Nov 2026)

**What happened [fact]:**
- On **20 November 2026**, Anthropic mathematician **Levent Alpöge** wrote: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis". He says it also covers the **generalized** RH and released it in the **Lean** proof assistant ([Al Jazeera](https://www.aljazeera.com/news/2026/11/21/riemann-hypothesis-has-the-worlds-most-famous-maths-problem-been-cracked), [Washington Post](https://www.washingtonpost.com/technology/2026/11/20/using-anthropic-ai-mathematician-claims-have-solved-riemann-hypothesis/), [IBM Think news](https://www.ibm.com/think/news/anthropic-claude-riemann-hypothesis-math-proof)).
- **Status: unconfirmed.** It runs to **over 17 million lines of Lean**, and mathematicians stress that a Lean formalization alone doesn't settle it ([Phys.org](https://phys.org/news/2026-11-sacred-mathematics-riemann-hypothesis-ai.html)).
- **Context:** in October 2026 an AI-produced proof of the weaker **"quasi-Riemann hypothesis"** was called "the most significant AI-for-math achievement so far" ([Quanta, 19 Oct 2026](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)).

**Cybersecurity implications [reasoning, careful]:**
- **It doesn't break RSA.** RH is about how *primes are distributed*. RSA's security rests on how hard it is to *factor* a product of two primes. A proof of RH doesn't give a factoring algorithm. Shor's algorithm ([[concepts/shors-algorithm]]) remains the known quantum threat, and it needs large fault-tolerant machines (resource estimates were cut to under one million noisy qubits for RSA-2048 in 2025 by Gidney) **[to verify: cite arXiv:2505.15917]**.
- **What it does touch:** many results in computational number theory are proved *assuming* GRH. For example, the Miller primality test is deterministic and polynomial-time *if* GRH holds (AKS already gives an unconditional test). A proof would turn those conditional results into theorems. That tightens the theory under cryptographic parameter choices, but it isn't an attack. **[reasoning, textbook background]**
- **The bigger signal [opinion]:** in 2026, AI is producing *verifiable* frontier mathematics. The same toolchain (LLMs + formal verification) can audit cryptographic proofs and protocol specs, and can search for **classical** algorithms that erode claimed quantum advantages, which is exactly the "claims withdrawn as classical improves" dynamic Gambetta described.

**Link to the three papers [reasoning]:** all three were benchmarked against *classical* simulation ("hard to compute classically", "chemical accuracy vs exact", "agreement with a noisy device model"). If AI accelerates classical algorithms, the bar for quantum simulation keeps rising. The FeMoco classical result above is an example. **Potential quantum advantage must be demonstrated against the best classical algorithms for the specified observable and error tolerance; Zhang-style dynamics is a candidate, not a guaranteed moat.** That's another reason, in hindsight, why the chosen paper ages well.


> [!note]- 🔗 Wiki connections for §5
> - **RSA and why primes matter:** [[concepts/rsa-cryptosystem#^key-generation]], [[concepts/rsa-cryptosystem#^encrypt-decrypt]].
> - **The actual quantum threat:** [[concepts/shors-algorithm#^reduction-summary]] and its [[concepts/shors-algorithm#^circuit-qiskit|N = 15 circuit]]; [[concepts/phase-estimation#^uses]].
> - **The response:** [[concepts/post-quantum-cryptography#^why-now]], [[concepts/post-quantum-cryptography#^pqc-response]], [[concepts/post-quantum-cryptography#^mosca-inequality]].
> - **Classical methods raising the bar:** [[concepts/quantum-simulation#^quantum-inspired]] (DMRG → PEPS/MERA) and the external note [DMRG for Dummies](/mit-raw/external/dmrg-for-dummies.md).

---

## 6. Sources to quote, by type (as the assignment encourages)

**Nature** (the course's main source):
- [[papers/zhang-2017-53-ion-dynamical-phase-transition|Zhang et al. 2017]] (chosen, [[mit-raw/external/papers/zhang-2017-53-ion-dpt-arxiv-1708.01044.pdf|local PDF]]); Bernien et al. 2017 (Lukin, 51 atoms, same issue) **[to verify: exact citation Nature 551, 579]**.
- Haghshenas et al. 2026, *Digital quantum magnetism on a trapped-ion quantum computer*, doi:10.1038/s41586-026-10445-3.
- Ransford et al. 2026, *A 98-qubit trapped-ion quantum computer with all-to-all connectivity*, doi:10.1038/s41586-026-10676-4, plus a News & Views piece.

**The Economist** (used in the course's other Reflect & Review material):
- *"Quantum computers promise mathematical superpowers"*, Science & technology, 29 Jul 2026 ([critique](https://postquantum.com/industry-news/economist-quantum-article-review/)).
- *"Quantum technology is beginning to come into its own"* (Technology Quarterly essay, 2017). It's attached in MIT xPRO's own support files ([xpro zendesk attachment](https://xpro.zendesk.com/hc/en-us/article_attachments/34182431455643)), a clue that it's course material. **[to verify which page uses it]**
- *Babbage* podcast episode on quantum computing (2 Sep 2026), from draft 001. **[to verify: episode title and date]**

**Podcasts:**
- *The New Quantum Era* (Sebastian Hassinger): "Quantum Advantage Achieved with Dominik Hangleiter" (1 Apr 2026), and an episode on the FeMoco classical-solution preprint ([Audible](https://www.audible.com/pd/The-New-Quantum-Era-Podcast/episodes/B0B844T3WC)).
- *Quantum Computing Report* (GQI) interview series, including Sebastian Hassinger (1 Jun 2026) ([QCR podcasts](https://quantumcomputingreport.com/podcasts/)).
- *The Post-Quantum World* (Protiviti): "2026 Predictions and the Road to 40,000 Logical Qubits" ([Protiviti](https://www.protiviti.com/fr-fr/podcast/2026-predictions-40000-logical-qubits-photonic)).
- Qiskit and PennyLane: IBM's *Qiskit* YouTube channel and Xanadu/PennyLane blogs and videos are well-known learning channels. **[to verify: whether either runs a current podcast series]**

**Press, 2017 (for the timing argument):** Physics World, IEEE Spectrum, HPCwire, Optica OPN, UMD release (29–30 Nov 2017); MIT Technology Review, AP, Science News, Bloomberg (IBM, 10 Nov 2017).

---

## 6A. Venture sprint follow-up (2026-11-24)

- [[analyses/femoco-classical-benchmark-2026]] — October journal publication, full source and abstract link, technical limitations, classical vs quantum comparison.
- [[analyses/qimono-venture-pilot]] — replaces earlier illustrative allocation with two alternative $275k budgets including $25k local SpinQ lab, four proposed experts, six-month Gantt, ISO readiness, angel pitch and mobile-first intake plan.
- [[analyses/qimono-assessment-slides]] — seven-slide Markdown demo with store QR placeholders.

## 7. Next steps
- [ ] Collect comparable media corpus and citation metrics for XYZ.
- [ ] Validate historical Rigetti vacancy counts and specific overlapping procurement opportunities.
- [ ] Refine hypothetical pilot with domain expert and actual client constraints.
- [ ] Read full FeMoco preprint and evaluate active-space and accuracy assumptions.
- [ ] Watch IBM's "State of the Union" video and replace §4's press-based facts with direct quotes and timestamps.
- [ ] Verify the [to verify] items (Bernien citation, Babbage episode, Bitcoin/AlphaGo background, Gidney estimate).
- [ ] Choose the forum "highlight" (best candidates: the Q1 thesis sentence or the Q2 paragraph).
- [ ] Cut a **150–300-word** version for the eDX box (the earlier 270-word version is in the private pack).
- [ ] Draft 2 peer replies (5-step template).

*Draft 001 (Grok, ~3,200 words) remains the private research notes. Its 2026 qubit table needs the same fact-check pass.*
