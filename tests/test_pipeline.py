import importlib
import sys
import types
from pathlib import Path
import subprocess
import shutil

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

TEST_DATA = ROOT / 'test_data' / 'Demo_Data'

# Fixture to provide fake nipype module so imports work
@pytest.fixture(autouse=True)
def fake_nipype(monkeypatch):
    fake = types.SimpleNamespace(Workflow=object, Node=object, Function=object)
    monkeypatch.setitem(sys.modules, 'nipype', fake)
    yield
    monkeypatch.delitem(sys.modules, 'nipype', raising=False)

def test_make_paths_bids_root(monkeypatch):
    mod = importlib.import_module('core.pipeline.io_workflow')
    make_paths = mod.make_paths
    t1, atlas = make_paths('sub-IndivConn000002', str(TEST_DATA), '', 'atlas.nii.gz')
    expected = TEST_DATA / 'sub-IndivConn000002' / 'ses-01' / 'anat' / 'sub-IndivConn000002_ses-01_run-01_T1w.nii.gz'
    assert Path(t1) == expected
    assert atlas == 'atlas.nii.gz'

def test_make_paths_reference(monkeypatch):
    mod = importlib.import_module('core.pipeline.io_workflow')
    make_paths = mod.make_paths
    t1, atlas = make_paths('subj', '', 'ref.nii.gz', 'atlas.nii.gz')
    assert t1 == 'ref.nii.gz'
    assert atlas == 'atlas.nii.gz'

def test_make_paths_errors(monkeypatch):
    mod = importlib.import_module('core.pipeline.io_workflow')
    make_paths = mod.make_paths
    with pytest.raises(ValueError):
        make_paths('subj', '', '', 'atlas.nii.gz')
    with pytest.raises(ValueError):
        make_paths('subj', '', 'ref.nii.gz', '')

def test_apply_parcellation(monkeypatch, tmp_path):
    mod = importlib.import_module('core.pipeline.parc_workflow')
    apply_parcellation = mod.apply_parcellation

    # Fake external tools
    true_cmd = shutil.which('true') or '/bin/true'
    def fake_which(tool):
        return true_cmd
    monkeypatch.setattr(shutil, 'which', fake_which)

    calls = []
    def fake_run(cmd, check):
        calls.append(cmd)
        return subprocess.CompletedProcess(cmd, 0)
    monkeypatch.setattr(subprocess, 'run', fake_run)

    out = apply_parcellation('t1.nii.gz', 'atlas.nii.gz', out_dir=tmp_path)
    expected = tmp_path / 'atlas_in_subject.nii.gz'
    assert Path(out) == expected
    # two commands should be executed: bet and flirt
    assert len(calls) == 2

def test_linear_register(monkeypatch, tmp_path):
    mod = importlib.import_module('core.pipeline.linear_reg_workflow')
    linear_register = mod.linear_register

    true_cmd = shutil.which('true') or '/bin/true'
    def fake_which(tool):
        return true_cmd
    monkeypatch.setattr(shutil, 'which', fake_which)

    calls = []
    def fake_run(cmd, check):
        calls.append(cmd)
        return subprocess.CompletedProcess(cmd, 0)
    monkeypatch.setattr(subprocess, 'run', fake_run)

    out = linear_register('img.nii.gz', 'ref.nii.gz', out_dir=tmp_path)
    expected = tmp_path / 'img_reg.nii.gz'
    assert Path(out) == expected
    assert len(calls) == 1

def test_build_subject_dict(monkeypatch):
    mod = importlib.import_module('core.pipeline.subjectdict_workflow')
    build_subject_dict = mod.build_subject_dict
    result = build_subject_dict('subj', 't1.nii.gz', 'labels.nii.gz')
    assert result == {
        'subject_id': 'subj',
        't1_file': 't1.nii.gz',
        'label_map': 'labels.nii.gz'
    }
