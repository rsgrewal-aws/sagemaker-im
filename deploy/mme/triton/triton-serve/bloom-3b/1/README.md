---
license: bigscience-bloom-rail-1.0
language:
- ak
- ar
- as
- bm
- bn
- ca
- code
- en
- es
- eu
- fon
- fr
- gu
- hi
- id
- ig
- ki
- kn
- lg
- ln
- ml
- mr
- ne
- nso
- ny
- or
- pa
- pt
- rn
- rw
- sn
- st
- sw
- ta
- te
- tn
- ts
- tum
- tw
- ur
- vi
- wo
- xh
- yo
- zh
- zhs
- zht
- zu
pipeline_tag: text-generation
model-index:
- name: bloom
  results:
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: arc_challenge
      type: arc_challenge
    metrics:
    - name: acc
      type: acc
      value: 0.27986348122866894
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: arc_easy
      type: arc_easy
    metrics:
    - name: acc
      type: acc
      value: 0.5946969696969697
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: axb
      type: axb
    metrics:
    - name: acc
      type: acc
      value: 0.4433876811594203
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: axg
      type: axg
    metrics:
    - name: acc
      type: acc
      value: 0.5
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: boolq
      type: boolq
    metrics:
    - name: acc
      type: acc
      value: 0.6165137614678899
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: cb
      type: cb
    metrics:
    - name: acc
      type: acc
      value: 0.30357142857142855
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: cola
      type: cola
    metrics:
    - name: acc
      type: acc
      value: 0.610738255033557
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: copa
      type: copa
    metrics:
    - name: acc
      type: acc
      value: 0.63
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: crows_pairs_english
      type: crows_pairs_english
    metrics:
    - name: acc
      type: acc
      value: 0.4973166368515206
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: crows_pairs_french
      type: crows_pairs_french
    metrics:
    - name: acc
      type: acc
      value: 0.5032796660703638
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: diabla
      type: diabla
    metrics:
    - name: acc
      type: acc
      value: 0.28888308977035493
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_afr
      type: gsarti/flores_101_afr
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.500798737976343
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_amh
      type: gsarti/flores_101_amh
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.9726863338897145
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ara
      type: gsarti/flores_101_ara
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.8083841089875814
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_asm
      type: gsarti/flores_101_asm
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.699102962086425
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ast
      type: gsarti/flores_101_ast
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.9252047073429384
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_azj
      type: gsarti/flores_101_azj
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.942805054270002
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_bel
      type: gsarti/flores_101_bel
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.614136245847082
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ben
      type: gsarti/flores_101_ben
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.121491534300969
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_bos
      type: gsarti/flores_101_bos
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.653353469118798
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_bul
      type: gsarti/flores_101_bul
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.7014693938055068
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_cat
      type: gsarti/flores_101_cat
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.305190041967345
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ceb
      type: gsarti/flores_101_ceb
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.291000321323428
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ces
      type: gsarti/flores_101_ces
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.447322753586386
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ckb
      type: gsarti/flores_101_ckb
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.7255124939234765
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_cym
      type: gsarti/flores_101_cym
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 12.539424151448149
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_dan
      type: gsarti/flores_101_dan
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.183309001005672
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_deu
      type: gsarti/flores_101_deu
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.1180422286591347
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ell
      type: gsarti/flores_101_ell
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.467943456164706
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_eng
      type: gsarti/flores_101_eng
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.018740628193298
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_est
      type: gsarti/flores_101_est
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 9.11654425176368
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_fas
      type: gsarti/flores_101_fas
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.058009097116482
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_fin
      type: gsarti/flores_101_fin
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.847047959628553
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_fra
      type: gsarti/flores_101_fra
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.9975177011840075
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ful
      type: gsarti/flores_101_ful
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 11.465912731488828
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_gle
      type: gsarti/flores_101_gle
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.681491663539422
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_glg
      type: gsarti/flores_101_glg
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.029991089015508
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_guj
      type: gsarti/flores_101_guj
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.955224230286231
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_hau
      type: gsarti/flores_101_hau
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 10.758347356372159
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_heb
      type: gsarti/flores_101_heb
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.6004478129801667
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_hin
      type: gsarti/flores_101_hin
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.712530650588064
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_hrv
      type: gsarti/flores_101_hrv
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.822418943372185
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_hun
      type: gsarti/flores_101_hun
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.440482646965992
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_hye
      type: gsarti/flores_101_hye
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.657718918347166
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ibo
      type: gsarti/flores_101_ibo
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.564814003872672
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ind
      type: gsarti/flores_101_ind
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.1597101468869373
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_isl
      type: gsarti/flores_101_isl
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.082349269518136
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ita
      type: gsarti/flores_101_ita
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.9687591414176207
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_jav
      type: gsarti/flores_101_jav
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.0573805415708994
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_jpn
      type: gsarti/flores_101_jpn
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.7758864197116933
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kam
      type: gsarti/flores_101_kam
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 11.072949642861332
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kan
      type: gsarti/flores_101_kan
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.551730651007082
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kat
      type: gsarti/flores_101_kat
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.522630524283745
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kaz
      type: gsarti/flores_101_kaz
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.3901748516975574
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kea
      type: gsarti/flores_101_kea
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.918534182590863
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kir
      type: gsarti/flores_101_kir
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.729278369847201
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_kor
      type: gsarti/flores_101_kor
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.932884847226212
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_lao
      type: gsarti/flores_101_lao
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.9077314760849924
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_lav
      type: gsarti/flores_101_lav
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.777221919194806
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_lin
      type: gsarti/flores_101_lin
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.524842908050988
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_lit
      type: gsarti/flores_101_lit
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.369179434621725
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ltz
      type: gsarti/flores_101_ltz
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.801059747949214
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_lug
      type: gsarti/flores_101_lug
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.483203026364786
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_luo
      type: gsarti/flores_101_luo
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 11.975963093623681
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mal
      type: gsarti/flores_101_mal
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.615948455160037
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mar
      type: gsarti/flores_101_mar
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.483253482821379
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mkd
      type: gsarti/flores_101_mkd
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.9656732291754087
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mlt
      type: gsarti/flores_101_mlt
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 15.004773437665275
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mon
      type: gsarti/flores_101_mon
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.410598542315402
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mri
      type: gsarti/flores_101_mri
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.474035895661322
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_msa
      type: gsarti/flores_101_msa
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.5710001772665634
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_mya
      type: gsarti/flores_101_mya
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.413577969878331
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_nld
      type: gsarti/flores_101_nld
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.127831721885065
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_nob
      type: gsarti/flores_101_nob
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.402763169129877
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_npi
      type: gsarti/flores_101_npi
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.199342701937889
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_nso
      type: gsarti/flores_101_nso
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.154626800955667
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_nya
      type: gsarti/flores_101_nya
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.179860208369393
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_oci
      type: gsarti/flores_101_oci
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.8617357393685845
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_orm
      type: gsarti/flores_101_orm
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 12.911595421079408
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ory
      type: gsarti/flores_101_ory
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.189421861225964
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_pan
      type: gsarti/flores_101_pan
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.698477289331806
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_pol
      type: gsarti/flores_101_pol
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.625550458479643
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_por
      type: gsarti/flores_101_por
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.9754515986213523
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_pus
      type: gsarti/flores_101_pus
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.4963371422771585
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ron
      type: gsarti/flores_101_ron
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.965456830031304
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_rus
      type: gsarti/flores_101_rus
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.0498020542445303
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_slk
      type: gsarti/flores_101_slk
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.450822127057479
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_slv
      type: gsarti/flores_101_slv
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 6.620252120186232
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_sna
      type: gsarti/flores_101_sna
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.462166771382726
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_snd
      type: gsarti/flores_101_snd
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.466066951221973
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_som
      type: gsarti/flores_101_som
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 11.95918054093392
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_spa
      type: gsarti/flores_101_spa
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.8965140104323535
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_srp
      type: gsarti/flores_101_srp
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.871214785885079
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_swe
      type: gsarti/flores_101_swe
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.054972008155866
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_swh
      type: gsarti/flores_101_swh
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.6973091886730676
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tam
      type: gsarti/flores_101_tam
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.539493400469833
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tel
      type: gsarti/flores_101_tel
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.807499987508966
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tgk
      type: gsarti/flores_101_tgk
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 3.5994818827380426
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tgl
      type: gsarti/flores_101_tgl
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.667053833119858
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tha
      type: gsarti/flores_101_tha
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.365940201944242
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_tur
      type: gsarti/flores_101_tur
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 4.885014749844601
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_ukr
      type: gsarti/flores_101_ukr
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.7240934990288483
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_umb
      type: gsarti/flores_101_umb
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 12.766915508610673
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_urd
      type: gsarti/flores_101_urd
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.9797467071381232
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_uzb
      type: gsarti/flores_101_uzb
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 12.002337637722146
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_vie
      type: gsarti/flores_101_vie
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 1.76578415476397
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_wol
      type: gsarti/flores_101_wol
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 9.144285650306488
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_xho
      type: gsarti/flores_101_xho
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 7.403240538286952
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_yor
      type: gsarti/flores_101_yor
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 5.91272037551173
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_zho_simpl
      type: gsarti/flores_101_zho_simpl
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.2769070822768533
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_zho_trad
      type: gsarti/flores_101_zho_trad
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 2.5180582198242383
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: gsarti/flores_101_zul
      type: gsarti/flores_101_zul
    metrics:
    - name: byte_perplexity
      type: byte_perplexity
      value: 8.53353320693145
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: headqa
      type: headqa
    metrics:
    - name: acc
      type: acc
      value: 0.26440554339897887
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: hellaswag
      type: hellaswag
    metrics:
    - name: acc
      type: acc
      value: 0.41236805417247563
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: logiqa
      type: logiqa
    metrics:
    - name: acc
      type: acc
      value: 0.2073732718894009
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: mathqa
      type: mathqa
    metrics:
    - name: acc
      type: acc
      value: 0.24958123953098826
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: mc_taco
      type: mc_taco
    metrics:
    - name: em
      type: em
      value: 0.11936936936936937
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: mnli
      type: mnli
    metrics:
    - name: acc
      type: acc
      value: 0.35496688741721855
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: mnli_mismatched
      type: mnli_mismatched
    metrics:
    - name: acc
      type: acc
      value: 0.35211554109031734
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: mrpc
      type: mrpc
    metrics:
    - name: acc
      type: acc
      value: 0.5857843137254902
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: multirc
      type: multirc
    metrics:
    - name: acc
      type: acc
      value: 0.5375412541254125
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: openbookqa
      type: openbookqa
    metrics:
    - name: acc
      type: acc
      value: 0.216
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: piqa
      type: piqa
    metrics:
    - name: acc
      type: acc
      value: 0.7078346028291621
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: prost
      type: prost
    metrics:
    - name: acc
      type: acc
      value: 0.22683603757472245
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: pubmedqa
      type: pubmedqa
    metrics:
    - name: acc
      type: acc
      value: 0.616
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: qnli
      type: qnli
    metrics:
    - name: acc
      type: acc
      value: 0.5072304594545122
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: qqp
      type: qqp
    metrics:
    - name: acc
      type: acc
      value: 0.3842443729903537
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: race
      type: race
    metrics:
    - name: acc
      type: acc
      value: 0.3521531100478469
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: rte
      type: rte
    metrics:
    - name: acc
      type: acc
      value: 0.47653429602888087
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: sciq
      type: sciq
    metrics:
    - name: acc
      type: acc
      value: 0.892
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: sst
      type: sst
    metrics:
    - name: acc
      type: acc
      value: 0.5177752293577982
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: triviaqa
      type: triviaqa
    metrics:
    - name: acc
      type: acc
      value: 0.041633518960487934
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: tydiqa_primary
      type: tydiqa_primary
    metrics:
    - name: acc
      type: acc
      value: 0.3011337608795236
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: webqs
      type: webqs
    metrics:
    - name: acc
      type: acc
      value: 0.01673228346456693
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: wic
      type: wic
    metrics:
    - name: acc
      type: acc
      value: 0.5015673981191222
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: winogrande
      type: winogrande
    metrics:
    - name: acc
      type: acc
      value: 0.5864246250986582
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: wnli
      type: wnli
    metrics:
    - name: acc
      type: acc
      value: 0.471830985915493
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: wsc
      type: wsc
    metrics:
    - name: acc
      type: acc
      value: 0.4423076923076923
      verified: false
  - task:
      type: text-generation
      name: text generation
    dataset:
      name: humaneval
      type: humaneval
    metrics:
    - name: pass@1
      type: pass@1
      value: 0.15524390243902436
      verified: false
    - name: pass@10
      type: pass@10
      value: 0.3220367632383857
      verified: false
    - name: pass@100
      type: pass@100
      value: 0.5545431515723145
      verified: false
---

<h1 style='text-align: center '>BLOOM LM</h1> 
<h2 style='text-align: center '><em>BigScience Large Open-science Open-access Multilingual Language Model</em> </h2> 
<h3 style='text-align: center '>Model Card</h3>
<img src="https://s3.amazonaws.com/moonup/production/uploads/1657124309515-5f17f0a0925b9863e28ad517.png" alt="BigScience Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

Version 1.0 / 26.May.2022

## Table of Contents
1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Training Data](#training-data)
4. [Risks and Limitations](#risks-and-limitations)
5. [Evaluation](#evaluation)
6. [Recommendations](#recommendations)
7. [Glossary and Calculations](#glossary-and-calculations)
8. [More Information](#more-information)
9. [Model Card Authors](#model-card-authors)

## Model Details  

### Basics
*This section provides information for anyone who wants to know about the model.*

<details>
<summary>Click to expand</summary> <br/>
    
**Developed by:** BigScience ([website](https://bigscience.huggingface.co))

* All collaborators are either volunteers or have an agreement with their employer. *(Further breakdown of participants forthcoming.)*
    
**Model Type:** Transformer-based Language Model

**Version:** 1.0.0

**Languages:** Multiple; see [training data](#training-data)

**License:** RAIL License v1.0 ([link](https://huggingface.co/spaces/bigscience/license))

**Release Date Estimate:** Monday, 11.July.2022

**Send Questions to:** bigscience-contact@googlegroups.com

**Cite as:** BigScience, _BigScience Language Open-science Open-access Multilingual (BLOOM) Language Model_. International, May 2021-May 2022

**Funded by:** 
    
* The French government.

* Hugging Face ([website](https://huggingface.co)).

* Organizations of contributors.  *(Further breakdown of organizations forthcoming.)*

</details>

### Technical Specifications
*This section provides information for people who work on model development.*

<details>
<summary>Click to expand</summary><br/>

Please see [the BLOOM training README](https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml#readme) for full details on replicating training.

**Model Architecture:** Modified from Megatron-LM GPT2 (see [paper](https://arxiv.org/abs/1909.08053), [BLOOM Megatron code](https://github.com/bigscience-workshop/Megatron-DeepSpeed)):

* Decoder-only architecture

* Layer normalization applied to word embeddings layer (`StableEmbedding`; see [code](https://github.com/facebookresearch/bitsandbytes), [paper](https://arxiv.org/pdf/2110.02861.pdf))

* ALiBI positional encodings (see [paper](https://arxiv.org/pdf/2108.12409.pdf)), with GeLU activation functions

* 3,002,557,440 parameters:

    * 642,252,800 embedding parameters

    * 30 layers, 32 attention heads

    * Hidden layers are 2560-dimensional

    * Sequence length of 2048 tokens used (see [BLOOM tokenizer](https://huggingface.co/bigscience/tokenizer), [tokenizer description](#tokenization))

**Objective Function:** Cross Entropy with mean reduction (see [API documentation](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss)).
    
**Compute infrastructure:** Jean Zay Public Supercomputer, provided by the French government (see [announcement](https://www.enseignementsup-recherche.gouv.fr/fr/signature-du-marche-d-acquisition-de-l-un-des-supercalculateurs-les-plus-puissants-d-europe-46733)).

* Hardware: 384 A100 80GB GPUs (48 nodes):
    
    * Additional 32 A100 80GB GPUs (4 nodes) in reserve

    *  8 GPUs per node Using NVLink 4 inter-gpu connects, 4 OmniPath links

    *   CPU: AMD

    *   CPU memory: 512GB per node

    *   GPU memory: 640GB per node

    *   Inter-node connect: Omni-Path Architecture (OPA)

    *   NCCL-communications network: a fully dedicated subnet

    *   Disc IO network: shared network with other types of nodes

* Software:
  
    *   Megatron-DeepSpeed ([Github link](https://github.com/bigscience-workshop/Megatron-DeepSpeed))

    *   DeepSpeed ([Github link](https://github.com/microsoft/DeepSpeed))

    *   PyTorch (pytorch-1.11 w/ CUDA-11.5; see [Github link](https://github.com/pytorch/pytorch))

    *   apex ([Github link](https://github.com/NVIDIA/apex))


#### **Training**

Training logs: [Tensorboard link](https://huggingface.co/tensorboard/bigscience/tr11c-2B5-logs)

- Number of epochs: 1 (*current target*)

- Dates:
    
    - Started 11th March, 2022 11:42am PST

    - Ended 5th July, 2022

- Estimated cost of training: Equivalent of $2-5M in cloud computing (including preliminary experiments)

- Server training location: Île-de-France, France

#### **Tokenization**
    
The BLOOM tokenizer ([link](https://huggingface.co/bigscience/tokenizer)) is a learned subword tokenizer trained using:
    
- A byte-level Byte Pair Encoding (BPE) algorithm 

- A simple pre-tokenization rule, no normalization

- A vocabulary size of 250,680

It was trained on a subset of a preliminary version of the corpus using alpha-weighting per language.    
    
</details>


### Environmental Impact

<details>
<summary>Click to expand</summary><br/>

The training supercomputer, Jean Zay ([website](http://www.idris.fr/eng/jean-zay/jean-zay-presentation-eng.html)), uses mostly nuclear energy. The heat generated by it is reused for heating campus housing.
    
**Estimated carbon emissions:**  *(Forthcoming upon completion of training.)*
    
**Estimated electricity usage:** *(Forthcoming upon completion of training.)*


</details>
<p>&nbsp;</p>

## Uses

*This section addresses questions around how the model is intended to be used, discusses the foreseeable users of the model (including those affected by the model), and describes uses that are considered out of scope or misuse of the model. 
It provides information for anyone considering using the model or who is affected by the model.*


<details>
<summary>Click to expand</summary><br/>
    
### Intended Use

This model is being created in order to enable public research on large language models (LLMs). LLMs are intended to be used for language generation or as a pretrained base model that can be further fine-tuned for specific tasks. Use cases below are not exhaustive.

#### **Direct Use**

-   Text generation

-   Exploring characteristics of language generated by a language model

    -   Examples: Cloze tests, counterfactuals, generations with reframings

#### **Downstream Use**

-   Tasks that leverage language models include: Information Extraction, Question Answering, Summarization

### Misuse and Out-of-scope Use
*This section addresses what users ought not do with the model.*

See the [BLOOM License](https://huggingface.co/spaces/bigscience/license), Attachment A, for detailed usage restrictions. The below list is non-exhaustive, but lists some easily foreseeable problematic use cases.

#### **Out-of-scope Uses**

Using the model in [high-stakes](#high-stakes) settings is out of scope for this model.  The model is not designed for [critical decisions](#critical-decisions) nor uses with any material consequences on an individual's livelihood or wellbeing. The model outputs content that appears factual but is not correct.  

##### Out-of-scope Uses Include:

-   Usage in biomedical domains, political and legal domains, or finance domains

-   Usage for evaluating or scoring individuals, such as for employment, education, or credit

-   Applying the model for critical automatic decisions, generating factual content, creating reliable summaries, or generating predictions that must be correct

#### **Misuse**

Intentionally using the model for harm, violating [human rights](#human-rights), or other kinds of malicious activities, is a misuse of this model. This includes:

-   Spam generation

-   Disinformation and influence operations

-   Disparagement and defamation

-   Harassment and abuse
  
-   [Deception](#deception)

-   Unconsented impersonation and imitation

-   Unconsented surveillance 

-   Generating content without attribution to the model, as specified in the [RAIL License, Use Restrictions](https://huggingface.co/spaces/bigscience/license)

### Intended Users

#### **Direct Users**

-   General Public

-   Researchers

-   Students

-   Educators

-   Engineers/developers

-   Non-commercial entities

-   Community advocates, including human and civil rights groups

#### Indirect Users

-   Users of derivatives created by Direct Users, such as those using software with an [intended use](#intended-use)

-   Users of [Derivatives of the Model, as described in the License](https://huggingface.co/spaces/bigscience/license)

#### Others Affected (Parties Prenantes)

-   People and groups referred to by the LLM

-   People and groups exposed to outputs of, or decisions based on, the LLM

-   People and groups whose original work is included in the LLM
    
</details>
<p>&nbsp;</p>

## Training Data
*This section provides a high-level overview of the training data. It is relevant for anyone who wants to know the basics of what the model is learning.*


<details>
<summary>Click to expand</summary><br/>
    
Details for each dataset are provided in individual [Data Cards](https://huggingface.co/spaces/bigscience/BigScienceCorpus).

Training data includes:

-   45 natural languages
    
-   12 programming languages

-   In 1.5TB of pre-processed text, converted into 350B unique tokens (see [the tokenizer section](#tokenization) for more.)


#### **Languages**
    
The pie chart shows the distribution of languages in training data.
   
![pie chart showing the distribution of languages in training data](https://github.com/bigscience-workshop/model_card/blob/main/assets/data/pie_chart.svg?raw=true)


The following table shows the further distribution of Niger-Congo and Indic languages in the training data.
<details>
<summary>Click to expand</summary><br/>
    
| Niger Congo    | Percentage |         | Indic     | Percentage |
|----------------|------------ |------  |-----------|------------|
| Chi Tumbuka    | 0.00002    |         | Assamese  | 0.01       |
| Kikuyu         | 0.00004    |         | Odia      | 0.04       |
| Bambara        | 0.00004    |         | Gujarati  | 0.04       |
| Akan           | 0.00007    |         | Marathi   | 0.05       |
| Xitsonga       | 0.00007    |         | Punjabi   | 0.05       |
| Sesotho        | 0.00007    |         | Kannada   | 0.06       |
| Chi Chewa      | 0.0001     |         | Nepali    | 0.07       |
| Setswana       | 0.0002     |         | Telugu    | 0.09       |
| Northern Sotho | 0.0002     |         | Malayalam | 0.10       |
| Fon            | 0.0002     |         | Urdu      | 0.10       |
| Kirundi        | 0.0003     |         | Tamil     | 0.20       |
| Wolof          | 0.0004     |         | Bengali   | 0.50       |
| Kuganda        | 0.0004     |         | Hindi     | 0.70       |
| Chi Shona      | 0.001      |
| Isi Zulu       | 0.001      |
| Igbo           | 0.001      |
| Xhosa          | 0.001      |
| Kinyarwanda    | 0.003      |
| Yoruba         | 0.006      |
| Swahili        | 0.02       |
</details>

The following table shows the distribution of programming languages.
<details>
<summary>Click to expand</summary><br/>
    
| Extension      | Language   | Number of files |
|----------------|------------|-----------------|
| java           | Java       | 5,407,724       |
| php            | PHP        | 4,942,186       |
| cpp            | C++        | 2,503,930       |
| py             | Python     | 2,435,072       |
| js             | JavaScript | 1,905,518       |
| cs             | C#         | 1,577,347       |
| rb             | Ruby       | 6,78,413        |
| cc             | C++        | 443,054         |
| hpp            | C++        | 391,048         |
| lua            | Lua        | 352,317         |
| go             | GO         | 227,763         |
| ts             | TypeScript | 195,254         |
| C              | C          | 134,537         |
| scala          | Scala      | 92,052          |
| hh             | C++        | 67,161          |
| H              | C++        | 55,899          |
| tsx            | TypeScript | 33,107          |
| rs             | Rust       | 29,693          |
| phpt           | PHP        | 9,702           |
| c++            | C++        | 1,342           |
| h++            | C++        | 791             |
| php3           | PHP        | 540             |
| phps           | PHP        | 270             |
| php5           | PHP        | 166             |
| php4           | PHP        | 29              |
    
</details>    
</details>
<p>&nbsp;</p>

## Risks and Limitations
*This section identifies foreseeable harms and misunderstandings.*

<details>
<summary>Click to expand</summary><br/>
    
Model may:

-   Overrepresent some viewpoints and underrepresent others

-   Contain stereotypes
  
-   Contain [personal information](#personal-data-and-information)

-   Generate:

    -   Hateful, abusive, or violent language

    -   Discriminatory or prejudicial language

    -   Content that may not be appropriate for all settings, including sexual content

-   Make errors, including producing incorrect information as if it were factual

-   Generate irrelevant or repetitive outputs
</details>
<p>&nbsp;</p>

## Evaluation
*This section describes the evaluation protocols and provides the results.*

<details>
<summary>Click to expand</summary><br/>

### Metrics 
*This section describes the different ways performance is calculated and why.*
    
Includes:

| Metric             | Why chosen                                                         |
|--------------------|--------------------------------------------------------------------|
| [Perplexity](#perplexity)         | Standard metric for quantifying model improvements during training |
| Cross Entropy [Loss](#loss) | Standard objective for language models.                            |

And multiple different metrics for specific tasks. _(More evaluation metrics forthcoming upon completion of evaluation protocol.)_

### Factors 
*This section lists some different aspects of BLOOM models. Its focus is on aspects that are likely to give rise to high variance in model behavior.*

- Language, such as English or Yoruba

- Domain, such as newswire or stories
    
- Demographic characteristics, such as gender or nationality

###  Results
*Results are based on the [Factors](#factors) and [Metrics](#metrics).*

**Zero-shot evaluations:**

See this repository for JSON files: https://github.com/bigscience-workshop/evaluation-results

| Task | Language | Metric | BLOOM-2B5 |
|:----|:----|:----|:----:|
| arc_challenge | eng | acc ↑ | 0.28 |
| arc_easy | eng | acc ↑ | 0.595 |
| axb (Median of 10 prompts) | eng | acc ↑ | 0.443 |
| axg (Median of 10 prompts) | eng | acc ↑ | 0.5 |
| boolq (Median of 11 prompts) | eng | acc ↑ | 0.617 |
| cb (Median of 15 prompts) | eng | acc ↑ | 0.304 |
| cola (Median of 5 prompts) | eng | acc ↑ | 0.611 |
| copa (Median of 9 prompts) | eng | acc ↑ | 0.63 |
| crows_pairs_english (Median of 6 prompts) | eng | acc ↑ | 0.497 |
| crows_pairs_french (Median of 7 prompts) | fra | acc ↑ | 0.503 |
| diabla (Median of 2 prompts) | eng | acc ↑ | 0.289 |
| gsarti/flores_101_afr | afr | byte_perplexity ↓ | 6.501 |
| gsarti/flores_101_amh | amh | byte_perplexity ↓ | 3.973 |
| gsarti/flores_101_ara | ara | byte_perplexity ↓ | 1.808 |
| gsarti/flores_101_asm | asm | byte_perplexity ↓ | 5.699 |
| gsarti/flores_101_ast | ast | byte_perplexity ↓ | 3.925 |
| gsarti/flores_101_azj | azj | byte_perplexity ↓ | 6.943 |
| gsarti/flores_101_bel | bel | byte_perplexity ↓ | 3.614 |
| gsarti/flores_101_ben | ben | byte_perplexity ↓ | 5.121 |
| gsarti/flores_101_bos | bos | byte_perplexity ↓ | 5.653 |
| gsarti/flores_101_bul | bul | byte_perplexity ↓ | 2.701 |
| gsarti/flores_101_cat | cat | byte_perplexity ↓ | 2.305 |
| gsarti/flores_101_ceb | ceb | byte_perplexity ↓ | 6.291 |
| gsarti/flores_101_ces | ces | byte_perplexity ↓ | 5.447 |
| gsarti/flores_101_ckb | ckb | byte_perplexity ↓ | 3.726 |
| gsarti/flores_101_cym | cym | byte_perplexity ↓ | 12.539 |
| gsarti/flores_101_dan | dan | byte_perplexity ↓ | 5.183 |
| gsarti/flores_101_deu | deu | byte_perplexity ↓ | 3.118 |
| gsarti/flores_101_ell | ell | byte_perplexity ↓ | 2.468 |
| gsarti/flores_101_eng | eng | byte_perplexity ↓ | 2.019 |
| gsarti/flores_101_est | est | byte_perplexity ↓ | 9.117 |
| gsarti/flores_101_fas | fas | byte_perplexity ↓ | 3.058 |
| gsarti/flores_101_fin | fin | byte_perplexity ↓ | 6.847 |
| gsarti/flores_101_fra | fra | byte_perplexity ↓ | 1.998 |
| gsarti/flores_101_ful | ful | byte_perplexity ↓ | 11.466 |
| gsarti/flores_101_gle | gle | byte_perplexity ↓ | 8.681 |
| gsarti/flores_101_glg | glg | byte_perplexity ↓ | 3.03 |
| gsarti/flores_101_guj | guj | byte_perplexity ↓ | 4.955 |
| gsarti/flores_101_hau | hau | byte_perplexity ↓ | 10.758 |
| gsarti/flores_101_heb | heb | byte_perplexity ↓ | 3.6 |
| gsarti/flores_101_hin | hin | byte_perplexity ↓ | 4.713 |
| gsarti/flores_101_hrv | hrv | byte_perplexity ↓ | 5.822 |
| gsarti/flores_101_hun | hun | byte_perplexity ↓ | 6.44 |
| gsarti/flores_101_hye | hye | byte_perplexity ↓ | 3.658 |
| gsarti/flores_101_ibo | ibo | byte_perplexity ↓ | 5.565 |
| gsarti/flores_101_ind | ind | byte_perplexity ↓ | 2.16 |
| gsarti/flores_101_isl | isl | byte_perplexity ↓ | 8.082 |
| gsarti/flores_101_ita | ita | byte_perplexity ↓ | 2.969 |
| gsarti/flores_101_jav | jav | byte_perplexity ↓ | 7.057 |
| gsarti/flores_101_jpn | jpn | byte_perplexity ↓ | 2.776 |
| gsarti/flores_101_kam | kam | byte_perplexity ↓ | 11.073 |
| gsarti/flores_101_kan | kan | byte_perplexity ↓ | 5.552 |
| gsarti/flores_101_kat | kat | byte_perplexity ↓ | 2.523 |
| gsarti/flores_101_kaz | kaz | byte_perplexity ↓ | 3.39 |
| gsarti/flores_101_kea | kea | byte_perplexity ↓ | 8.919 |
| gsarti/flores_101_kir | kir | byte_perplexity ↓ | 3.729 |
| gsarti/flores_101_kor | kor | byte_perplexity ↓ | 3.933 |
| gsarti/flores_101_lao | lao | byte_perplexity ↓ | 2.908 |
| gsarti/flores_101_lav | lav | byte_perplexity ↓ | 7.777 |
| gsarti/flores_101_lin | lin | byte_perplexity ↓ | 7.525 |
| gsarti/flores_101_lit | lit | byte_perplexity ↓ | 7.369 |
| gsarti/flores_101_ltz | ltz | byte_perplexity ↓ | 8.801 |
| gsarti/flores_101_lug | lug | byte_perplexity ↓ | 8.483 |
| gsarti/flores_101_luo | luo | byte_perplexity ↓ | 11.976 |
| gsarti/flores_101_mal | mal | byte_perplexity ↓ | 4.616 |
| gsarti/flores_101_mar | mar | byte_perplexity ↓ | 5.483 |
| gsarti/flores_101_mkd | mkd | byte_perplexity ↓ | 2.966 |
| gsarti/flores_101_mlt | mlt | byte_perplexity ↓ | 15.005 |
| gsarti/flores_101_mon | mon | byte_perplexity ↓ | 3.411 |
| gsarti/flores_101_mri | mri | byte_perplexity ↓ | 7.474 |
| gsarti/flores_101_msa | msa | byte_perplexity ↓ | 2.571 |
| gsarti/flores_101_mya | mya | byte_perplexity ↓ | 2.414 |
| gsarti/flores_101_nld | nld | byte_perplexity ↓ | 4.128 |
| gsarti/flores_101_nob | nob | byte_perplexity ↓ | 5.403 |
| gsarti/flores_101_npi | npi | byte_perplexity ↓ | 5.199 |
| gsarti/flores_101_nso | nso | byte_perplexity ↓ | 8.155 |
| gsarti/flores_101_nya | nya | byte_perplexity ↓ | 8.18 |
| gsarti/flores_101_oci | oci | byte_perplexity ↓ | 4.862 |
| gsarti/flores_101_orm | orm | byte_perplexity ↓ | 12.912 |
| gsarti/flores_101_ory | ory | byte_perplexity ↓ | 5.189 |
| gsarti/flores_101_pan | pan | byte_perplexity ↓ | 4.698 |
| gsarti/flores_101_pol | pol | byte_perplexity ↓ | 4.626 |
| gsarti/flores_101_por | por | byte_perplexity ↓ | 1.975 |
| gsarti/flores_101_pus | pus | byte_perplexity ↓ | 4.496 |
| gsarti/flores_101_ron | ron | byte_perplexity ↓ | 4.965 |
| gsarti/flores_101_rus | rus | byte_perplexity ↓ | 2.05 |
| gsarti/flores_101_slk | slk | byte_perplexity ↓ | 6.451 |
| gsarti/flores_101_slv | slv | byte_perplexity ↓ | 6.62 |
| gsarti/flores_101_sna | sna | byte_perplexity ↓ | 8.462 |
| gsarti/flores_101_snd | snd | byte_perplexity ↓ | 5.466 |
| gsarti/flores_101_som | som | byte_perplexity ↓ | 11.959 |
| gsarti/flores_101_spa | spa | byte_perplexity ↓ | 1.897 |
| gsarti/flores_101_srp | srp | byte_perplexity ↓ | 2.871 |
| gsarti/flores_101_swe | swe | byte_perplexity ↓ | 5.055 |
| gsarti/flores_101_swh | swh | byte_perplexity ↓ | 3.697 |
| gsarti/flores_101_tam | tam | byte_perplexity ↓ | 4.539 |
| gsarti/flores_101_tel | tel | byte_perplexity ↓ | 5.807 |
| gsarti/flores_101_tgk | tgk | byte_perplexity ↓ | 3.599 |
| gsarti/flores_101_tgl | tgl | byte_perplexity ↓ | 5.667 |
| gsarti/flores_101_tha | tha | byte_perplexity ↓ | 2.366 |
| gsarti/flores_101_tur | tur | byte_perplexity ↓ | 4.885 |
| gsarti/flores_101_ukr | ukr | byte_perplexity ↓ | 2.724 |
| gsarti/flores_101_umb | umb | byte_perplexity ↓ | 12.767 |
| gsarti/flores_101_urd | urd | byte_perplexity ↓ | 1.98 |
| gsarti/flores_101_uzb | uzb | byte_perplexity ↓ | 12.002 |
| gsarti/flores_101_vie | vie | byte_perplexity ↓ | 1.766 |
| gsarti/flores_101_wol | wol | byte_perplexity ↓ | 9.144 |
| gsarti/flores_101_xho | xho | byte_perplexity ↓ | 7.403 |
| gsarti/flores_101_yor | yor | byte_perplexity ↓ | 5.913 |
| gsarti/flores_101_zho_simpl | zho_simpl | byte_perplexity ↓ | 2.277 |
| gsarti/flores_101_zho_trad | zho_trad | byte_perplexity ↓ | 2.518 |
| gsarti/flores_101_zul | zul | byte_perplexity ↓ | 8.534 |
| headqa | esp | acc ↑ | 0.264 |
| hellaswag | eng | acc ↑ | 0.412 |
| logiqa | eng | acc ↑ | 0.207 |
| mathqa | eng | acc ↑ | 0.25 |
| mc_taco | eng | em ↑ | 0.119 |
| mnli (Median of 15 prompts) | eng | acc ↑ | 0.355 |
| mnli_mismatched (Median of 15 prompts) | eng | acc ↑ | 0.352 |
| mrpc | eng | acc ↑ | 0.586 |
| multirc (Median of 11 prompts) | eng | acc ↑ | 0.538 |
| openbookqa | eng | acc ↑ | 0.216 |
| piqa | eng | acc ↑ | 0.708 |
| prost | eng | acc ↑ | 0.227 |
| pubmedqa | eng | acc ↑ | 0.616 |
| qnli | eng | acc ↑ | 0.507 |
| qqp (Median of 7 prompts) | eng | acc ↑ | 0.384 |
| race | eng | acc ↑ | 0.352 |
| rte (Median of 6 prompts) | eng | acc ↑ | 0.477 |
| sciq | eng | acc ↑ | 0.892 |
| sst (Median of 6 prompts) | eng | acc ↑ | 0.518 |
| triviaqa | eng | acc ↑ | 0.042 |
| tydiqa_primary (Median of 24 prompts) | eng | acc ↑ | 0.301 |
| webqs | eng | acc ↑ | 0.017 |
| wic (Median of 11 prompts) | eng | acc ↑ | 0.502 |
| winogrande | eng | acc ↑ | 0.586 |
| wnli (Median of 6 prompts) | eng | acc ↑ | 0.472 |
| wsc (Median of 11 prompts) | eng | acc ↑ | 0.442 |
| humaneval | python | pass@1 ↑ | 0.155 |
| humaneval | python | pass@10 ↑ | 0.322 |
| humaneval | python | pass@100 ↑ | 0.555 |

**Train-time Evaluation:**

As of 25.May.2022, 15:00 PST:

- Training Loss: 2.0

- Validation Loss: 2.2

- Perplexity: 8.9

</details>
<p>&nbsp;</p>

## Recommendations

*This section provides information on warnings and potential mitigations.*


<details>
<summary>Click to expand</summary><br/>

-   Indirect users should be made aware when the content they're working with is created by the LLM.

-   Users should be aware of [Risks and Limitations](#risks-and-limitations), and include an appropriate age disclaimer or blocking interface as necessary.

-   Models pretrained with the LLM should include an updated Model Card.

-   Users of the model should provide mechanisms for those affected to provide feedback, such as an email address for comments.

</details>
<p>&nbsp;</p>

## Glossary and Calculations

*This section defines common terms and how metrics are calculated.*



<details>
<summary>Click to expand</summary><br/>

-   <a name="loss">**Loss:**</a> A calculation of the difference between what the model has learned and what the data shows ("groundtruth"). The lower the loss, the better. The training process aims to minimize the loss. 

-   <a name="perplexity">**Perplexity:**</a> This is based on what the model estimates the probability of new data is. The lower the perplexity, the better.  If the model is 100% correct at predicting the next token it will see, then the perplexity is 1. Mathematically this is calculated using entropy. 

-   <a name="high-stakes">**High-stakes settings:**</a> Such as those identified as "high-risk AI systems" and "unacceptable risk AI systems" in the European Union's proposed [Artificial Intelligence (AI) Act](https://artificialintelligenceact.eu/annexes/).

-   <a name="critical-decisions">**Critical decisions:**</a> Such as those defined in [the United States' proposed Algorithmic Accountability Act](https://www.congress.gov/117/bills/s3572/BILLS-117s3572is.pdf).

-   <a name="human-rights">**Human rights:**</a> Includes those rights defined in the [Universal Declaration of Human Rights](https://www.un.org/sites/un2.un.org/files/2021/03/udhr.pdf).

-  <a name="personal-data-and-information">**Personal Data and Personal Information:**</a> Personal data and information is defined in multiple data protection regulations, such as "[personal data](https://gdpr-info.eu/issues/personal-data/)" in the [European Union's General Data Protection Regulation](https://gdpr-info.eu); and "personal information" in the Republic of South Africa's [Protection of Personal Information Act](https://www.gov.za/sites/default/files/gcis_document/201409/3706726-11act4of2013popi.pdf), The People's Republic of China's [Personal information protection law](http://en.npc.gov.cn.cdurl.cn/2021-12/29/c_694559.htm).
  
- <a name="sensitive-characteristics">**Sensitive characteristics:**</a> This includes specifically protected categories in human rights (see [UHDR, Article 2](https://www.un.org/sites/un2.un.org/files/2021/03/udhr.pdf)) and personal information regulation (see GDPR, [Article 9; Protection of Personal Information Act, Chapter 1](https://www.gov.za/sites/default/files/gcis_document/201409/3706726-11act4of2013popi.pdf))

- <a name="deception">**Deception:**</a> Doing something to intentionally mislead individuals to believe something that is false, such as by creating deadbots or chatbots on social media posing as real people, or generating text documents without making consumers aware that the text is machine generated.

</details>
<p>&nbsp;</p>

## More Information

<details>
<summary>Click to expand</summary><br/>
    
### Dataset Creation

Blog post detailing the design choices during the dataset creation: https://bigscience.huggingface.co/blog/building-a-tb-scale-multilingual-dataset-for-language-modeling

### Technical Specifications

Blog post summarizing how the architecture, size, shape, and pre-training duration where selected: https://bigscience.huggingface.co/blog/what-language-model-to-train-if-you-have-two-million-gpu-hours

More details on the architecture/optimizer: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml

Blog post on the hardware/engineering side: https://bigscience.huggingface.co/blog/which-hardware-to-train-a-176b-parameters-model

Details on the distributed setup used for the training: https://github.com/bigscience-workshop/bigscience/tree/master/train/tr11-176B-ml

Tensorboard updated during the training: https://huggingface.co/bigscience/tr11-176B-ml-logs/tensorboard#scalars&tagFilter=loss

Insights on how to approach training, negative results: https://github.com/bigscience-workshop/bigscience/blob/master/train/lessons-learned.md

Details on the obstacles overcome during the preparation on the engineering side (instabilities, optimization of training throughput, so many technical tricks and questions): https://github.com/bigscience-workshop/bigscience/blob/master/train/tr11-176B-ml/chronicles.md

### Initial Results

Initial prompting experiments using interim checkpoints: https://huggingface.co/spaces/bigscience/bloom-book

</details>
<p>&nbsp;</p>
    
## Model Card Authors
*Ordered roughly chronologically and by amount of time spent.*

Margaret Mitchell, Giada Pistilli, Yacine Jernite, Ezinwanne Ozoani, Marissa Gerchick, Nazneen Rajani, Sasha Luccioni, Irene Solaiman, Maraim Masoud, Somaieh Nikpoor, Carlos Muñoz Ferrandis, Stas Bekman, Christopher Akiki, Danish Contractor, David Lansky, Angelina McMillan-Major, Tristan Thrush, Suzana Ilić, Gérard Dupont, Shayne Longpre, Manan Dey, Stella Biderman, Douwe Kiela, Emi Baylor, Teven Le Scao, Aaron Gokaslan, Julien Launay, Niklas Muennighoff

