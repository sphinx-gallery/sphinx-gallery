from pathlib import Path
from xml.etree.ElementTree import parse

import pytest

# Configure test parameters and file path of the JUnit xml file
MAX_EXECUTION_TIME = 5.0  # Tests fail if greater than this value
# Same value as `sphinx_gallery_conf['junit']` in `conf.py`
CONF_JUNIT = Path("sphinx-gallery") / "junit-results.xml"
# Full xml path relative to this test module
XML_PATH = Path(__file__).parents[2] / "doc" / "_build" / "html" / CONF_JUNIT

xml_root = parse(XML_PATH).getroot()
test_cases = [dict(case.attrib) for case in xml_root.iterfind("testcase")]
test_ids = [case["classname"] for case in test_cases]


@pytest.mark.parametrize("testcase", test_cases, ids=test_ids)
def test_gallery_example(testcase):
    if float(testcase["time"]) > MAX_EXECUTION_TIME:
        pytest.fail(
            f"Gallery example {testcase['name']!r} from {testcase['file']!r}\n"
            f"Took too long to run: Duration {testcase['time']}s > {MAX_EXECUTION_TIME}s",
        )
