
# Concept Schemes in this file

[Earth and Environmental Science specimen type extension](#EarthandEnvironmentalSciencespecimentypeextension)


This file generated at: "2023-07-07T13:21:17.763892+00:00"
---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#EarthandEnvironmentalSciencespecimentypeextension}

# **Concept scheme:** Earth and Environmental Science specimen type extension

Vocabulary last modified:  2023-07-07

subtitle: 
  This concept scheme contains skos concepts for categorizing kinds of Earth Material sample types, extending the iSamples Material Sample Type vocabulary. Defintions from SESAR, ODM2, wikipedia, ESS-DIVE, and other sources; sources are cited with each term.

Namespace: 
[`https://w3id.org/isample/1.0/esmaterialsample/sampletype`](https://w3id.org/isample/1.0/esmaterialsample/sampletype)

**History**

* 2023-07-07 SMR add solid material sample and broader relations from classes it subsumes.

- [genericaggregation](#genericaggregation)
    - [Boxed core](#boxedcore)
    - [Composite sample](#compositesample)
        - [Chip Channel Sample](#chipchannelsample)
        - [High Grade Sample](#highgradesample)
    - [Core Catcher](#corecatcher)
    - [Cuttings](#cuttings)
    - [Dredge](#dredge)
    - [Magnetic fraction](#magneticfraction)
    - [Material Captured in Filter](#materialcapturedinfilter)
    - [Mechanical fraction](#mechanicalfraction)
    - [Mineral separate](#mineralseparate)
    - [Non-magnetic fraction](#nonmagneticfraction)
    - [Prepared powder](#preparedpowder)
        - [Prepared rock powder](#preparedrockpowder)
    - [Trawl](#trawl)

- [bundlebiomeaggregation](#bundlebiomeaggregation)
    - [Cell culture](#cellculture)

- [fluidincontainer](#fluidincontainer)
    - [Filtrate](#filtrate)

- [othersolidobject](#othersolidobject)
    - [Core](#core)
    - [Core half round](#corehalfround)
    - [Core peice](#corepeice)
    - [Core quarter round](#corequarterround)
    - [Core section](#coresection)
    - [Core subpeice](#coresubpeice)
    - [Dust wipe](#dustwipe)
    - [Individual solid cube](#individualsolidcube)
    - [Individual solid cylinder](#individualsolidcylinder)
    - [Mineral specimen](#mineralspecimen)
    - [Rock hand sample](#rockhandsample)
    - [Slab](#slab)
    - [U-channel sample](#uchannelsample)

- [analyticalpreparation](#analyticalpreparation)
    - [Cell culture](#cellculture)
    - [Dissolved chemical fraction](#dissolvedchemicalfraction)
    - [FIB lamella](#fiblamella)
    - [Glass slide smear](#glassslidesmear)
    - [Individual solid cube](#individualsolidcube)
    - [Magnetic fraction](#magneticfraction)
    - [Mechanical fraction](#mechanicalfraction)
    - [Mineral separate](#mineralseparate)
    - [Mounted section](#mountedsection)
        - [Polished thin section](#polishedthinsection)
        - [Thick section](#thicksection)
        - [Thin section](#thinsection)
        - [Ultra thin section](#ultrathinsection)
    - [Non-magnetic fraction](#nonmagneticfraction)
    - [Peel](#peel)
    - [Prepared powder](#preparedpowder)
        - [Prepared rock powder](#preparedrockpowder)
    - [Pressed pellet](#pressedpellet)
    - [Slab](#slab)

- [Solid material sample](#solidmaterialsample)
    - [FIB lamella](#fiblamella)
    - [Glass slide smear](#glassslidesmear)
    - [Mounted section](#mountedsection)
        - [Polished thin section](#polishedthinsection)
        - [Thick section](#thicksection)
        - [Thin section](#thinsection)
        - [Ultra thin section](#ultrathinsection)
    - [Peel](#peel)
    - [Pressed pellet](#pressedpellet)

**Concepts**

[]{#genericaggregation}

##  `https://w3id.org/isample/vocabulary/specimentype/0.9/genericaggregation`

- Child of:
 [`solidmaterialsample`](#solidmaterialsample)

- Concept URI token: genericaggregation


[]{#boxedcore}

###  Boxed core


- Child of:
 [`genericaggregation`](#genericaggregation)

- A collection of core peices that are stored in an individual box.

- **Source:**
this vocabulary

- Concept URI token: boxedcore


[]{#compositesample}

###  Composite sample


- Child of:
 [`genericaggregation`](#genericaggregation)

- an aggregation of small chips of uniform rock material collected
over a large area (generally greater than 2.5m across). These are the
ideal 'representative' samples used in mineral exploration. A
composite sample might be collected to determine the background values
of trace elements in a particular type of rock, or to determine if ore
grade mineralization is present over a large area.

- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling

- Concept URI token: compositesample


[]{#chipchannelsample}

####  Chip Channel Sample


- Child of:
 [`compositesample`](#compositesample)

- small chips of rock collected over a specified interval, with the
objective to obtain a representative sample for that interval. Most of
the time chip channel samples are collected in succession along a
sample line which is laid out in advance using a tape.  The freshest
material possible is sampled, preferably chipping directly from
bedrock. Sample intervals are set at a specified width, usually
ranging from 30cm to 7m. Due to the method of sampling, chip channel
samples tend to be rather large (up to 20 pounds for a five foot
interval)

- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling

- Concept URI token: chipchannelsample


[]{#highgradesample}

####  High Grade Sample


- Child of:
 [`compositesample`](#compositesample)

- in mineral exploration, selective pieces of the most highly
mineralized material from a mineralize site, intentionally excluding
less mineralized material. A high grade sample might be collected to
indicate what the best possible values are, or to provide material for
certain types of trace element analyses.

- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling

- Concept URI token: highgradesample


[]{#corecatcher}

###  Core Catcher


- Child of:
 [`genericaggregation`](#genericaggregation)

- material recovered from the core catcher of a sedimentary core and
which is treated as a separate section from the core. The core catcher
is a device at the bottom of the core barrel that prevents the core
from sliding out while the barrel is retrieved from the hole.
(http://publications.iodp.org/proceedings/323/102/102_.htm)

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: corecatcher


[]{#cuttings}

###  Cuttings


- Child of:
 [`genericaggregation`](#genericaggregation)

- unconsolidated Earth material produced by the grinding action of a
drill bit during drilling of a borehole.

- **Source:**
http://vocabulary.odm2.org/specimentype/cuttings/

- Concept URI token: cuttings


[]{#dredge}

###  Dredge


- Child of:
 [`genericaggregation`](#genericaggregation)

- an aggregation of material sampled by dragging a collection bucket
(dredge) across the bottom of a water body

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: dredge


[]{#magneticfraction}

###  Magnetic fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.

- **Source:**
this vocabulary

- Concept URI token: magneticfraction


[]{#materialcapturedinfilter}

###  Material Captured in Filter


- Child of:
 [`genericaggregation`](#genericaggregation)

- A material sample captured in filter, for example from a water
sample that was filtered. Must be associated with filter size field.

- **Source:**
https://github.com/ess-dive-community/essdive-sample-id-metadata/blob/master/terms/objectType.md

- Concept URI token: materialcapturedinfilter


[]{#mechanicalfraction}

###  Mechanical fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.

- **Source:**
this vocabulary

- Concept URI token: mechanicalfraction


[]{#mineralseparate}

###  Mineral separate


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- an aggregation of particles of the same mineral extracted and
concentrated from a rock.

- **Source:**
this vocabulary

- Concept URI token: mineralseparate


[]{#nonmagneticfraction}

###  Non-magnetic fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- collection of particles from a crushed rock sample based on their
lack of attraction to a magnet

- **Source:**
this vocabulary

- Concept URI token: nonmagneticfraction


[]{#preparedpowder}

###  Prepared powder


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)

- **Source:**
this vocabulary

- Concept URI token: preparedpowder


[]{#preparedrockpowder}

####  Prepared rock powder


- Child of:
 [`preparedpowder`](#preparedpowder)

- a powder manufactured by pulverizing a rock.

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: preparedrockpowder


[]{#trawl}

###  Trawl


- Child of:
 [`genericaggregation`](#genericaggregation)

- an aggregation of biogenic or non-biogenic material extracted from a
water body

- **Source:**
this vocabulary

- Concept URI token: trawl



[]{#bundlebiomeaggregation}

##  `https://w3id.org/isample/vocabulary/specimentype/0.9/bundlebiomeaggregation`

- Concept URI token: bundlebiomeaggregation


[]{#cellculture}

###  Cell culture


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`bundlebiomeaggregation`](#bundlebiomeaggregation)

- a collection of cells are grown under controlled conditions,
generally outside of their natural environment

- **Source:**
https://en.wikipedia.org/wiki/Cell_culture

- Concept URI token: cellculture



[]{#fluidincontainer}

##  `https://w3id.org/isample/vocabulary/specimentype/0.9/fluidincontainer`

- Concept URI token: fluidincontainer


[]{#filtrate}

###  Filtrate


- Child of:
 [`fluidincontainer`](#fluidincontainer)

- A sample that has gone through a filtration process to separate
solids from fluids (liquids or gases), using a filter medium through
which only the fluid can pass. Must be associated with a filter size.

- **Source:**
https://github.com/ess-dive-community/essdive-sample-id-metadata/blob/master/terms/objectType.md

- Concept URI token: filtrate



[]{#othersolidobject}

##  `https://w3id.org/isample/vocabulary/specimentype/0.9/othersolidobject`

- Child of:
 [`solidmaterialsample`](#solidmaterialsample)

- Concept URI token: othersolidobject


[]{#core}

###  Core


- Child of:
 [`othersolidobject`](#othersolidobject)

- Cylinder of rock or sediment extracted from within the earth, and
representing the entire sample extracted during a single borehole
drilling event.  Typically using some rotary drilling technology. In
many cases the core is extracted in segments that are 'core sections'.
A core from a single borehole is rarely a continous unbroken object;
commonly parts of the core will break up during drilling or
extraction, leaving gaps or sections that are granular material. Cores
are normally composed of consolidated ('solid') material, but in some
cases loosely consolidated material might be recovered, and considered
sediment or tephra. To be called 'core' the material must be
sufficiently consolidated to maintain a cylindrical shape. A core
hasPart (hasChild) 'Core section'

- **Source:**
this vocabulary

- Concept URI token: core


[]{#corehalfround}

###  Core half round


- Child of:
 [`othersolidobject`](#othersolidobject)

- Half-cylindrical peice of consolidated material produced by along-
axis split of a core whole round along a selected diameter .    Has
childOf relation to core section or core, core section, or Core peice
from which is was split

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: corehalfround


[]{#corepeice}

###  Core peice


- Child of:
 [`othersolidobject`](#othersolidobject)

- A cylindrical peice of consolidated earth material extracted as a
single solid object between breaks in recovery of core from a
borehole. has parent core section

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: corepeice


[]{#corequarterround}

###  Core quarter round


- Child of:
 [`othersolidobject`](#othersolidobject)

- a partial cylindrical peice of consolidated material created by
along-axis split of a core half round. Has Parent core half round

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: corequarterround


[]{#coresection}

###  Core section


- Child of:
 [`othersolidobject`](#othersolidobject)

- Segment of a core representing some interval along the well bore.
Child of Core

- **Source:**
https://www.geosamples.org/vocabularies

- Concept URI token: coresection


[]{#coresubpeice}

###  Core subpeice


- Child of:
 [`othersolidobject`](#othersolidobject)

- A peice of consolidated material broken from a core peice. has
Parent core peice or core section

- **Source:**
https://www.geosamples.org/vocabularies

- Concept URI token: coresubpeice


[]{#dustwipe}

###  Dust wipe


- Child of:
 [`othersolidobject`](#othersolidobject)

- a pre-weighed and packaged paper towel (wipe) used to wipe over a
surface to collect particulates from the surface

- **Source:**
https://www.cdc.gov/nceh/lead/docs/publications/Environmental_Sampling.pdf, dust wipe sampling

- Concept URI token: dustwipe


[]{#individualsolidcube}

###  Individual solid cube


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

- ? is this an anlytical preparation, or a decorative object?

- **Source:**


- Concept URI token: individualsolidcube


[]{#individualsolidcylinder}

###  Individual solid cylinder


- Child of:
 [`othersolidobject`](#othersolidobject)

- A cylindrical peice of consolidated material not obtained by
subsurface drilling.  Cores drilled for paleomagnetic analysis are a
common example. Tree ring cores are another...

- **Source:**
may be core, plug sample, drill a cylinder from a core

- Concept URI token: individualsolidcylinder


[]{#mineralspecimen}

###  Mineral specimen


- Child of:
 [`othersolidobject`](#othersolidobject)

- a solid object consisting of one particular mineral, or several
minerals intended to be representative of one or more of the mineral
species.

- **Source:**
this vocabulary

- Concept URI token: mineralspecimen


[]{#rockhandsample}

###  Rock hand sample


- Child of:
 [`othersolidobject`](#othersolidobject)

- individual peice of rock broken from an outcrop or larger peice of
rock.

- **Source:**
this vocabulary

- Concept URI token: rockhandsample


[]{#slab}

###  Slab


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

- a relatively planar rock sample,cut from a large sample to produce a
tabular peice of rock with the irregular outline of the original
sample on the diameter where the cut was mate.

- **Source:**
this vocabulary

- Concept URI token: slab


[]{#uchannelsample}

###  U-channel sample


- Child of:
 [`othersolidobject`](#othersolidobject)

- a rectangular prism of loosely consolidated sediment extracted from
a core segment. has parent core piece or core segment

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: uchannelsample



[]{#analyticalpreparation}

##  `https://w3id.org/isample/vocabulary/specimentype/0.9/analyticalpreparation`

- Concept URI token: analyticalpreparation


[]{#cellculture}

###  Cell culture


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`bundlebiomeaggregation`](#bundlebiomeaggregation)

- a collection of cells are grown under controlled conditions,
generally outside of their natural environment

- **Source:**
https://en.wikipedia.org/wiki/Cell_culture

- Concept URI token: cellculture


[]{#dissolvedchemicalfraction}

###  Dissolved chemical fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)

- This is about collection method, not speciment type. Analytical
preparation that is a solution concentrating some constituent of
interest from a parent sample.

- **Source:**


- Concept URI token: dissolvedchemicalfraction


[]{#fiblamella}

###  FIB lamella


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- very thin sheet of solid material milled from a larger sample using
a focused ion beam. Used for TEM analysis.

- **Source:**
this vocabulary

- Concept URI token: fiblamella


[]{#glassslidesmear}

###  Glass slide smear


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- sample from a cell culture spread into a thin layer on a glass slide
for optical investigation

- **Source:**
https://pubs.usgs.gov/of/2001/of01-041/htmldocs/methods/sslide.htm

- Concept URI token: glassslidesmear


[]{#individualsolidcube}

###  Individual solid cube


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

- ? is this an anlytical preparation, or a decorative object?

- **Source:**


- Concept URI token: individualsolidcube


[]{#magneticfraction}

###  Magnetic fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.

- **Source:**
this vocabulary

- Concept URI token: magneticfraction


[]{#mechanicalfraction}

###  Mechanical fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.

- **Source:**
this vocabulary

- Concept URI token: mechanicalfraction


[]{#mineralseparate}

###  Mineral separate


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- an aggregation of particles of the same mineral extracted and
concentrated from a rock.

- **Source:**
this vocabulary

- Concept URI token: mineralseparate


[]{#mountedsection}

###  Mounted section


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- a thin slice of a rock that has been mounted on a glass slide for
optical study

- **Source:**
this vocabulary

- Concept URI token: mountedsection


[]{#polishedthinsection}

####  Polished thin section


- Child of:
 [`mountedsection`](#mountedsection)

- a thin section that has its free surface polished until perfectly
planar and free of pits and scratches. Used for reflected light
petrography and for electron microprobe or SEM investigation.

- **Source:**
http://www.minsocam.org/ammin/AM53/AM53_2070.pdf

- Concept URI token: polishedthinsection


[]{#thicksection}

####  Thick section


- Child of:
 [`mountedsection`](#mountedsection)

- Thick sections are like thin sections, but milled to a greater
thickness. Typcially polished on one or both sides and used for fluid
or melt inclusion studies, Raman analyses, and infrared spectroscopy
analyses, and SEM or electron microprobe. The standard thickness for a
fluid inclusion thick section is 50 micrometers, but thick sections
can be made at any thickness.  Thick sections can be attached to a
glass slide, or can be prepared so that they can be removed from their
mount as a stand-alone slice of rock.

- **Source:**
https://viva.pressbooks.pub/analyticalmethodsingeosciences/chapter/2-2-thin-section-and-thick-section-anatomy/

- Concept URI token: thicksection


[]{#thinsection}

####  Thin section


- Child of:
 [`mountedsection`](#mountedsection)

- thin sliver of rock cut from a sample with a diamond saw and ground
optically flat, and then mounted on a glass slide and ground smooth
using progressively finer abrasive grit until the sample is 30 microns
thick.

- **Source:**
 https://en.wikipedia.org/wiki/Thin_section, 
http://vocabulary.odm2.org/specimentype/thinSection/ , 

- Concept URI token: thinsection


[]{#ultrathinsection}

####  Ultra thin section


- Child of:
 [`mountedsection`](#mountedsection)

- An ordinary thin section that is attached to the glass slide using a
soluble cement such as Canada balsam (soluble in ethanol) to allow
both sides to be worked on. The section is polished on both sides
using a fine diamond paste until it has a thickness in the range of
2-12 microns. This technique has been used to study the microstructure
of very fine-grained carbonate rocks, and also in the preparation of
mineral and rock specimens for transmission electron microscopy.

- **Source:**
http://vocabulary.odm2.org/specimentype/thinSection/  | https://en.wikipedia.org/wiki/Thin_section

- Concept URI token: ultrathinsection


[]{#nonmagneticfraction}

###  Non-magnetic fraction


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- collection of particles from a crushed rock sample based on their
lack of attraction to a magnet

- **Source:**
this vocabulary

- Concept URI token: nonmagneticfraction


[]{#peel}

###  Peel


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.

- **Source:**
https://strata.uga.edu/cincy/fauna/bryozoanStudy/acetatePeels.html

- Concept URI token: peel


[]{#preparedpowder}

###  Prepared powder


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`genericaggregation`](#genericaggregation)

- distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)

- **Source:**
this vocabulary

- Concept URI token: preparedpowder


[]{#preparedrockpowder}

####  Prepared rock powder


- Child of:
 [`preparedpowder`](#preparedpowder)

- a powder manufactured by pulverizing a rock.

- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object

- Concept URI token: preparedrockpowder


[]{#pressedpellet}

###  Pressed pellet


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- a sample prepared by grinding a parent sample to a fine powder,
mixing it with a binder, and pressing the mixture into a die at a
pressure of between 15 and 35 tons to produce a solid disc for
subsequent analysis, typically by X-Ray fluorescence.

- **Source:**


- Concept URI token: pressedpellet


[]{#slab}

###  Slab


- Child of:
 [`analyticalpreparation`](#analyticalpreparation)
 [`othersolidobject`](#othersolidobject)

- a relatively planar rock sample,cut from a large sample to produce a
tabular peice of rock with the irregular outline of the original
sample on the diameter where the cut was mate.

- **Source:**
this vocabulary

- Concept URI token: slab



[]{#solidmaterialsample}

##  Solid material sample


- Child of:
 [`physicalspecimen`](#physicalspecimen)

- a sample that is either a solid object or aggregation composed of
solid, non-biologic material. This is a generic class to allow for
poorly constrained sample descriptions, could be an aggregation or a
solid object, but is known not to be anthropogenic, fluid or
biological.

- **Source:**
this vocabulary

- Concept URI token: solidmaterialsample


[]{#fiblamella}

###  FIB lamella


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- very thin sheet of solid material milled from a larger sample using
a focused ion beam. Used for TEM analysis.

- **Source:**
this vocabulary

- Concept URI token: fiblamella


[]{#glassslidesmear}

###  Glass slide smear


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- sample from a cell culture spread into a thin layer on a glass slide
for optical investigation

- **Source:**
https://pubs.usgs.gov/of/2001/of01-041/htmldocs/methods/sslide.htm

- Concept URI token: glassslidesmear


[]{#mountedsection}

###  Mounted section


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- a thin slice of a rock that has been mounted on a glass slide for
optical study

- **Source:**
this vocabulary

- Concept URI token: mountedsection


[]{#polishedthinsection}

####  Polished thin section


- Child of:
 [`mountedsection`](#mountedsection)

- a thin section that has its free surface polished until perfectly
planar and free of pits and scratches. Used for reflected light
petrography and for electron microprobe or SEM investigation.

- **Source:**
http://www.minsocam.org/ammin/AM53/AM53_2070.pdf

- Concept URI token: polishedthinsection


[]{#thicksection}

####  Thick section


- Child of:
 [`mountedsection`](#mountedsection)

- Thick sections are like thin sections, but milled to a greater
thickness. Typcially polished on one or both sides and used for fluid
or melt inclusion studies, Raman analyses, and infrared spectroscopy
analyses, and SEM or electron microprobe. The standard thickness for a
fluid inclusion thick section is 50 micrometers, but thick sections
can be made at any thickness.  Thick sections can be attached to a
glass slide, or can be prepared so that they can be removed from their
mount as a stand-alone slice of rock.

- **Source:**
https://viva.pressbooks.pub/analyticalmethodsingeosciences/chapter/2-2-thin-section-and-thick-section-anatomy/

- Concept URI token: thicksection


[]{#thinsection}

####  Thin section


- Child of:
 [`mountedsection`](#mountedsection)

- thin sliver of rock cut from a sample with a diamond saw and ground
optically flat, and then mounted on a glass slide and ground smooth
using progressively finer abrasive grit until the sample is 30 microns
thick.

- **Source:**
 https://en.wikipedia.org/wiki/Thin_section, 
http://vocabulary.odm2.org/specimentype/thinSection/ , 

- Concept URI token: thinsection


[]{#ultrathinsection}

####  Ultra thin section


- Child of:
 [`mountedsection`](#mountedsection)

- An ordinary thin section that is attached to the glass slide using a
soluble cement such as Canada balsam (soluble in ethanol) to allow
both sides to be worked on. The section is polished on both sides
using a fine diamond paste until it has a thickness in the range of
2-12 microns. This technique has been used to study the microstructure
of very fine-grained carbonate rocks, and also in the preparation of
mineral and rock specimens for transmission electron microscopy.

- **Source:**
http://vocabulary.odm2.org/specimentype/thinSection/  | https://en.wikipedia.org/wiki/Thin_section

- Concept URI token: ultrathinsection


[]{#peel}

###  Peel


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.

- **Source:**
https://strata.uga.edu/cincy/fauna/bryozoanStudy/acetatePeels.html

- Concept URI token: peel


[]{#pressedpellet}

###  Pressed pellet


- Child of:
 [`solidmaterialsample`](#solidmaterialsample)
 [`analyticalpreparation`](#analyticalpreparation)

- a sample prepared by grinding a parent sample to a fine powder,
mixing it with a binder, and pressing the mixture into a die at a
pressure of between 15 and 35 tons to produce a solid disc for
subsequent analysis, typically by X-Ray fluorescence.

- **Source:**


- Concept URI token: pressedpellet



