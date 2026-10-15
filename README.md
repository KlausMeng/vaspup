# VASPUP

This is an old collection of scripts from 2014 to help set up VASP calculations.
The functionality has mostly been superceded by other packages such as
[materials-toolbox](https://github.com/utf/materials-toolbox) and
[kgrid](https://github.com/WMD-group/kgrid). These scripts are only kept here for posterity.

## Usage

### POTCAR generation

The `generate-potcar` script can be used to generate a VASP 
[POTCAR](https://cms.mpi.univie.ac.at/vasp/vasp/POTCAR_file.html) file, based on an input
POSCAR. If the current directory contains a POSCAR file, simply run:
```
generate-potcar
```
and the script will prompt you about which potentials you would like to use. Alternatively,
a POSCAR file can be specified as follows:
```
generate-potcar MgO/POSCAR
```
In order to enable this functionality, the `VASP_POTENTIALS` environment variable must be set
(see [Installation](#Installation) for more details).

If `VASP_POTENTIALS` points to a directory containing several potential sets, such as
`potpaw_PBE.64` and `potpaw_LDA.64`, the script will ask which set to use. You can also select
one directly:
```
generate-potcar --potential-set PBE.64
generate-potcar -p LDA.64 MgO/POSCAR
```
The same default can be set with the `VASP_POTENTIAL_SET` environment variable.

### Convergence Testing

The main functionality of this package is for quickly setting up a series of folders for 
convergence testing. To achieve this, create a folder called `input` containing INCAR, KPOINTS
POSCAR, and POTCAR files, in addition to a CONFIG file. An example CONFIG file is provided in
the [config directory](https://github.com/utf/vaspup/blob/master/config/CONVERGE) (NOTE: It must be
renamed from CONVERGE to CONFIG). The directory structure should match the below:

```bash
./<run script from here>
./input
    /INCAR
    /KPOINTS
    /POSCAR
    /POTCAR
    /CONFIG
```

Customise the CONFIG file as you wish, the run the `generate-converge` excutable from the folder **below** the 
`input` directory. A series of folders will be created, with the settings modified to match the folder names.

Once the calculations have finished running, the `data-converge` script can be used to extract the
total energies from the VASP output. The `data-converge` script should be run separately within the folders named
`kpoint_converge` and `cutoff_converge`.

### SOD Scripts

There are several scripts to help with automating the [Site-Occupancy Disorder](https://sites.google.com/site/rgrauc/sod-program)
package but I can't remember what these do exactly. I probably wouldn't go near them if I were you.

## Installation

Installation is simple, just update your path to include the location of the bin folder. E.g. Edit your `~/.bashrc`
file to include:

```bash
export PATH="${HOME}/path/to/vaspup/bin:${PATH}"
```

To enable the POTCAR functionality, you should also set the VASP_POTENTIALS environment variable to
point to your potentials directory. This can be a single potential set, or a parent directory
containing several sets. E.g. Edit your `~/.bashrc` file to include:

```bash
export VASP_POTENTIALS="${HOME}/path/to/vasp_pp"
export VASP_POTENTIAL_SET="PBE.64"
```

If `VASP_POTENTIAL_SET` is omitted and multiple potential sets are found, `generate-potcar` will
prompt you to choose one.

## Disclaimer

This program is not affiliated with VASP. This program is made available under the MIT License; you are free to modify and use the code, but do so at your own risk.


## Reproducible installation

This preservation branch contains the scripts used on ARCHER2 on 15 October 2026.
Install with `python -m pip install .`, or use a Git URL pinned to this branch's
full commit SHA in a Conda environment YAML. Scripts and their helper files are
installed together under the environment prefix; no source-checkout PATH edits
are needed. GNU/Linux, Bash and standard GNU command-line utilities are required;
`bc` is needed for numerical post-processing. VASP, licensed pseudopotentials and
the scheduler are supplied separately by the destination HPC.

The POTCAR set selector is preserved. Set `VASP_POTENTIALS` to the
licensed potential directory on the destination machine.

All legacy commands are available through `vaspup1 <command>` and
`vaspup1-<command>`. Unique commands retain their original names.
The overlapping `generate-converge` and `data-converge` names are reserved
for vaspup2, matching the original PATH precedence when both are installed.
The old SOD helpers still depend on external `~/scripts/data-*.sh` files
and SOD software; installing this package does not provide those dependencies.
