CreateDensity = \
"""
        CreateDensity<
            densityProfiles::densityProfile${name}${profile_index},
            startPosition::startPosition${name},
            PIC_${name}
        >"""

SetIonCharge = \
"""
        Manipulate<
            manipulators::SetIonCharge${name},
            PIC_${name}
        >,
        ManipulateDerive<
            manipulators::binary::UnboundElectronsTimesWeighting,
            PIC_${name},
            PIC_${TargetSpeciesName}
        >"""
