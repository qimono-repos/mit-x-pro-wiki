---
title: "Reflect & Review: draft 002 (brainstorm, no word limit)"
type: analysis
status: brainstorm
created: 2026-11-23
authors: Albert Gruning (opinions, framing), Claude Opus 5.5 (research, fact-check, structure)
assignment: "[[sources/week-4-08-reflect-and-review]]"
chosen_paper: "Zhang et al., Nature 551, 601–604 (2017)"
---

# Reflect & Review: draft 002

> **What this is.** A long brainstorm for the official Week 3 *Reflect & Review* activity ([source note](../sources/week-4-08-reflect-and-review.md)). There's no length limit here; the eDX box itself takes **150–300 words**, so a condensed version gets cut from this later. It builds on PAPER-DRAFT-001 (Grok, private Google Doc) and on the wiki: [[concepts/quantum-simulation]], [[concepts/quantum-annealing]], [[concepts/vqe]], [[concepts/quantum-chemistry]], [[concepts/photon-polarization-qubits]].
>
> **Tags used below:** **[fact]** = checked against a linked source on 2026-11-23 · **[opinion]** = Albert's position · **[reasoning]** = Claude's argument · **[to verify]** = not checked yet, don't publish as fact.

---

## 0. The three assigned papers, one line each

| # | Paper | Platform · institution | One-line takeaway |
|---|---|---|---|
| 1 | Zhang et al., *Observation of a many-body dynamical phase transition with a 53-qubit quantum simulator*, **Nature 551, 601–604 (30 Nov 2017)**. [arXiv:1708.01044](https://arxiv.org/abs/1708.01044) | 53 trapped ¹⁷¹Yb⁺ ions · JQI (University of Maryland + NIST), Monroe also IonQ | Analog simulation of a long-range transverse-field Ising model. Individual readout of every ion (~99%) lets them measure many-body correlations shot by shot, and they see a *dynamical* phase transition. **← chosen** |
| 2 | O'Malley et al., *Scalable quantum simulation of molecular energies*, **Phys. Rev. X 6, 031007 (2016)**. [arXiv:1512.06860](https://arxiv.org/abs/1512.06860) | Superconducting · Google + UCSB (+ Harvard, LBNL, Tufts, UCL) | H₂ energy curve via VQE (chemical accuracy) and Trotterized phase estimation. VQE is more robust to errors. |
| 3 | Kandala et al., *Hardware-efficient VQE for small molecules and quantum magnets*, **Nature 549, 242–246 (14 Sep 2017)**. [arXiv:1704.05018](https://arxiv.org/abs/1704.05018) | Superconducting · IBM T.J. Watson | Up to 6 qubits, 100+ Pauli terms, molecules up to BeH₂, plus a quantum magnet. Results match a noisy device model. |

Summaries: [external note](/mit-raw/external/reflect-review-papers.md).

---

## Q1. Impact on a business industry: was it the most influential of the three?

### Albert's thesis
**No, not in the press, and the reason is timing, not quality.** The press was busy with other stories, and quantum computing has a bad-press problem: hype, then backlash. **[opinion]**

### Evidence: the timing was brutal **[fact]**

1. **It shared the Nature issue with a rival record.** The same issue (Nature 551, 30 Nov 2017) carried Lukin's group (Harvard/MIT) with a **51-atom Rydberg simulator**. Physics World covered "two independent research groups" in one story ([Physics World, 29 Nov 2017](https://physicsworld.com/a/quantum-simulators-shed-new-light-on-magnetic-phase-transitions/)). Even UMD's own press release announced "two independent teams" with "more than 50" qubits ([UMD CMNS](https://cmns.umd.edu/news-events/news/quantum-simulators-wield-control-over-more-50-qubits-setting-new-record)). The headline was "50+ qubits", shared between two labs, not "53 ions".
2. **IBM had taken the "50-qubit" mainstream headline three weeks earlier.** On **10 Nov 2017** IBM announced a **50-qubit prototype** and a 20-qubit system on its cloud ([MIT Technology Review](https://www.technologyreview.com/2017/11/10/147728/ibm-raises-the-bar-with-a-50-qubit-quantum-computer/), [AP via Phys.org](https://phys.org/pdf429532312.pdf), [Science News](https://www.sciencenews.org/article/quantum-computing-steps-forward-50-qubit-prototype)). Bloomberg framed it as IBM vs Google in the race to "quantum supremacy" ([DataCenterKnowledge/Bloomberg](https://datacenterknowledge.com/supercomputers/ibm-ups-pressure-on-rivals-with-quantum-computer-prototype)). By 30 Nov the number "50" already belonged to a corporation in the public mind.
3. **Coverage stayed in specialist outlets.** The 53-ion result went to Physics World, IEEE Spectrum, HPCwire, Optica OPN and Nature Asia, the specialist science press ([IEEE Spectrum](https://spectrum.ieee.org/quantum-simulators-get-bigger-and-badder), [HPCwire](https://www.hpcwire.com/2017/11/29/two-quantum-simulators-cross-50-qubit-threshold/), [Optica OPN](https://www.optica-opn.org/home/newsroom/2017/december/quantum_simulators_leap_ahead)). The IBM announcement went through AP and Bloomberg to the business press.
4. **Even friendly coverage carried a disclaimer.** Physics World quoted Christine Muschik (Waterloo) calling these simulators "textbook examples of not being quantum computers", because they don't encode a complete gate set ([Physics World](https://physicsworld.com/a/quantum-simulators-shed-new-light-on-magnetic-phase-transitions/)). For a business reader that line reads as "not a product".
5. **Background [to verify before publishing]:** late 2017 was also the Bitcoin mania (peaking around mid-December 2017) and the AlphaGo Zero moment for AI (Nature, October 2017). Competing "future of computing" stories crowded the same news cycle.

### Evidence: quantum computing's bad-press cycle **[fact]**
- **Hype, then crash.** In January 2025 one sentence from Nvidia's Jensen Huang ("15 years… early side, 30… late side") sent IonQ, Rigetti and D-Wave down roughly 30–45% in a day ([Fortune](https://fortune.com/2025/01/09/nvidia-ceo-jensen-huang-tanks-quantum-computing-stocks/), [CNBC via NBC](https://nbcmiami.com/news/business/money-report/quantum-stocks-like-rigetti-plunge-after-nvidias-huang-says-the-computers-are-15-to-30-years-away/3509856)). One analyst's read: "any dollar chasing quantum computing stocks is not chasing AI stocks" ([Reuters via Cyprus Mail](https://cyprus-mail.com/2025/01/11/quantum-computing-stocks-take-a-hit-as-nvidia-ceo-predicts-long-road-ahead)). The press frames quantum *against* AI.
- **"Always five years away."** In August 2026 the cryptography mailing list was still circulating an essay titled "Why full-fledged quantum computers might always be five years away" ([metzdowd cryptography list](https://www.metzdowd.com/pipermail/cryptography/2026-August/039724.html)).
- **Even the best coverage gets corrected.** The Economist's 29 July 2026 feature, *"Quantum computers promise mathematical superpowers"*, was called "by a clear margin, the best quantum computing article I have seen", yet still "wrong" on several points by a practitioner reviewer ([PostQuantum review](https://postquantum.com/industry-news/economist-quantum-article-review/)).
- **Claims get withdrawn.** At IBM's own QDC 2026, Jay Gambetta's keynote described "classical researchers overtaking quantum results, claims being withdrawn as classical makes improvements" ([SiliconANGLE, 12 Nov 2026](https://siliconangle.com/?p=854010)). The field now says this openly.

### So what was its real business impact? **[reasoning]**
- **Industry: materials and magnetism, plus the trapped-ion hardware industry itself.** Zhang's paper simulated a quantum magnet, the model family behind magnetic materials and the same Ising Hamiltonian that [[concepts/quantum-annealing]] uses to encode optimization problems. Its direct business effect wasn't a product. It was **credibility capital** for trapped ions as a scalable, individually controllable platform.
- **The line from 2017 to 2026 is visible in Nature:**
  - 2026: *Digital quantum magnetism on a trapped-ion quantum computer* (Haghshenas et al., **Nature**, doi:10.1038/s41586-026-10445-3), Quantinuum hardware with TUM theory, "a regime in which classical computational methods begin to fail" ([TUM/MCQST](https://www.mcqst.de/news-and-events/news/quantum-computer-opens-a-new-path-to-practical-scientific-applications.html)). **[fact]** That's Zhang's question (quantum magnetism with ions) asked again with a *digital*, gate-based machine.
  - June 2026: Quantinuum's **98-qubit Helios**, "all-to-all connectivity", published in **Nature** ([Nature Asia summary](https://www.natureasia.com/ja-jp/phys-sci/research/15569), doi:10.1038/s41586-026-10676-4). **[fact]** All-to-all connectivity is exactly the property Zhang highlighted (long-range interactions, high connectivity).
  - Monroe, now at Duke, is still doing many-body simulations on ions, such as "string breaking" in particle physics using domain walls, a direct echo of the 2017 domain statistics ([Physics World](https://physicsworld.com/?p=130926)). **[fact]**
- **Was it the most influential of the three?** In the **press, no** (timing, a shared headline, "not a computer"). In **science and industry, arguably yes over the long run**: the chemistry-VQE line (papers 2 and 3) became an algorithm family everyone uses, but its "chemistry advantage" story keeps hitting classical counterattacks. For example, a January 2026 preprint claims a **classical solution of the FeMo-cofactor model to chemical accuracy** (Zhai et al., arXiv:2601.04621, discussed on *The New Quantum Era* podcast) ([Apple Podcasts show notes](https://podcasts.apple.com/us/podcast/the-new-quantum-era---innovation-in-quantum-computing,-science-and-technology/id1637676725)). **[fact, show-notes level; read the preprint before citing]** FeMoco is the nitrogenase cofactor, the same enzyme behind Chuang's Haber–Bosch example in our Week 3 chemistry lecture ([[concepts/quantum-chemistry]]). Meanwhile, the ion line kept growing into gate-model machines.

> **Candidate thesis sentence [opinion + reasoning]:** "Zhang et al. lost the 2017 press cycle (it shared a Nature issue with a 51-atom rival, three weeks after IBM's 50-qubit headline, and was labelled 'not a quantum computer'), but it won the decade: its signature properties, individual control and all-to-all connectivity, are the selling points of 2026's trapped-ion machines in Nature."

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

---

## 4. Personal insight A: IBM's "State of the Union" (QDC 2026) vs the 2016–17 papers

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
| Chemistry | H₂ with 2 effective qubits; BeH₂ with 6 | Protein–ligand "quantum-centric" simulations with Cleveland Clinic and RIKEN ([IBM Research](https://research.ibm.com/blog/ibm-think-2026-modeling-the-universe-with-quantum-computing)) |
| Scale | 6 qubits (IBM 2017) | 120 → 520 → 1,040 qubits (2025 → 2027) |
| Claim | "scalable", "hardware-efficient" | "advantage in 2026", "fault-tolerant by 2029" |
| Unchanged | **The VQE loop:** quantum state preparation + **classical** optimization ([[concepts/vqe]]) | still hybrid: "quantum-centric supercomputing" = QPU + HPC |

**Opinion hook [opinion]:** IBM's 2017 paper (Kandala) and IBM's 2026 roadmap share one idea, *hybrid*. What changed is the *size of the promise*. Zhang's group made no promise and shipped a physics result. The investor's job is to discount the promises and price the results.

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

**Link to the three papers [reasoning]:** all three were benchmarked against *classical* simulation ("hard to compute classically", "chemical accuracy vs exact", "agreement with a noisy device model"). If AI accelerates classical algorithms, the bar for quantum simulation keeps rising. The FeMoco classical result above is an example. **Quantum simulation's moat is physics a classical computer can't fake, which favours Zhang-style many-body dynamics over small-molecule energies.** That's another reason, in hindsight, why the chosen paper ages well.

---

## 6. Sources to quote, by type (as the assignment encourages)

**Nature** (the course's main source):
- Zhang et al. 2017 (chosen); Bernien et al. 2017 (Lukin, 51 atoms, same issue) **[to verify: exact citation Nature 551, 579]**.
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

## 7. Next steps
- [ ] Watch IBM's "State of the Union" video and replace §4's press-based facts with direct quotes and timestamps.
- [ ] Verify the [to verify] items (Bernien citation, Babbage episode, Bitcoin/AlphaGo background, Gidney estimate).
- [ ] Choose the forum "highlight" (best candidates: the Q1 thesis sentence or the Q2 paragraph).
- [ ] Cut a **150–300-word** version for the eDX box (the earlier 270-word version is in the private pack).
- [ ] Draft 2 peer replies (5-step template).

*Draft 001 (Grok, ~3,200 words) remains the private research notes. Its 2026 qubit table needs the same fact-check pass.*
