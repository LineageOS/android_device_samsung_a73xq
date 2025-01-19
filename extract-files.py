#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/samsung/sm7325-common',
    'vendor/qcom/opensource/display',
]


blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/hw/com.qti.chi.override.so': blob_fixup()
        .sig_replace(
            '80 06 40 F9 E1 78 00 94 80 01 00 34 82 DB FF D0 A3 DD FF F0 A5 DC FF 90 E6 03 00 2A',
            '1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5'
        )
        .sig_replace(
            '42 0C 0E 91 63 EC 0F 91 A5 20 1A 91 A4 11 80 52 E0 03 1F 2A 21 00 80 52 8D FE FF 97 80 06 40 F9',
            '1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 1F 20 03 D5 80 06 40 F9'
        ),
    'vendor/lib64/nfc_nci_nxpsn.so': blob_fixup()
        .replace_needed('libbase.so', 'libbase-v33.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'a73xq',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm7325-common', module.vendor
    )
    utils.run()
