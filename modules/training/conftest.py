import pytest
import asyncio
from playwright.sync_api import Playwright
from playwright.async_api import async_playwright
from datetime import datetime
from playwright.sync_api import sync_playwright
import os
from modules.frame_work.utility.custom_logger import log, CustomLogger
import allure

def pytest_addoption(parser):
    parser.addoption("--tbrowser", action="store", help="chrome")
    parser.addoption("--header-opt", action="store", help="chrome")
@pytest.fixture(scope="class")
def setup(request, playwright: Playwright):
    internet_browser = request.config.getoption("--tbrowser")
    execution_header = request.config.getoption("--header-opt")

    match execution_header:
        case 'headless':
            match internet_browser:
                case 'firefox':
                    browser = playwright.firefox.launch(headless=True,args=["--start-maximized"])
                    driver = browser.new_page()
                case 'webkit':
                    browser = playwright.webkit.launch(headless=True,args=["--start-maximized"])
                    driver = browser.new_page()
                case _:
                    browser = playwright.chromium.launch(headless=True,args=["--start-maximized"])
                    driver = browser.new_page()
        case _:
            match internet_browser:
                case 'firefox':
                    browser = playwright.firefox.launch(headless=False,args=["--start-maximized"])
                    driver = browser.new_page(no_viewport=True)
                case 'webkit':
                    browser = playwright.webkit.launch(headless=False,args=["--start-maximized"])
                    driver = browser.new_page(no_viewport=True)
                case _:
                    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
                    driver = browser.new_page(no_viewport=True)

    # driver.goto("http://112.199.119.250:82/ECP/auth/login")

    request.cls.driver = driver
    yield
    driver.close()

# # Configure reports directory
# REPORTS_DIR = "reports"
# SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
# VIDEOS_DIR = os.path.join(REPORTS_DIR, "videos")
# TRACES_DIR = os.path.join(REPORTS_DIR, "traces")

# @pytest.fixture(scope="session", autouse=True)
# def setup_reporting():
#     """Ensure reporting directories exist."""
#     for folder in [SCREENSHOTS_DIR, VIDEOS_DIR, TRACES_DIR]:
#         if not os.path.exists(folder):
#             os.makedirs(folder)

# @pytest.fixture(scope="session")
# def playwright():
#     with sync_playwright() as p:
#         yield p
#
# @pytest.fixture(scope="session")
# def browser(playwright, request):
#     browser_type = playwright.chromium
#     # You can extend this to read from a config or CLI
#     browser = browser_type.launch(headless=True, args=["--start-maximized"])
#     yield browser
#     browser.close()

# @pytest.fixture(scope="function")
# def context(browser, request):
#     # Enable video and trace recording
#     context = browser.new_context(
#         no_viewport=True,
#         record_video_dir=VIDEOS_DIR if request.config.getoption("--record-video") == "on" else None
#     )
#     # Start tracing
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#
#     yield context
#
#     # Context closure is handled after report checking in hook
#     context.close()

# @pytest.fixture(scope="function")
# def page(context):
#     page = context.new_page()
#     yield page
#     page.close()

# @pytest.fixture(scope="function")
# def context_args():
#     return {
#         "record_video_dir": "videos/"  # folder where videos will be saved
#     }
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     page = item.funcargs.get("page")
#     if not page:
#         return
#
#     if report.failed:
#         # Screenshot
#         screenshot = page.screenshot(full_page=True)
#         allure.attach(
#             screenshot,
#             name="Failure Screenshot",
#             attachment_type=allure.attachment_type.PNG
#         )
#
#         # Video
#         try:
#             video_path = page.video.path()
#             if video_path and os.path.exists(video_path):
#                 with open(video_path, "rb") as f:
#                     allure.attach(
#                         f.read(),
#                         name="Failure Video",
#                         attachment_type=allure.attachment_type.WEBM
#                     )
#         except Exception as e:
#             print(f"Could not attach video: {e}")
#
#     elif report.passed:
#         # Clean up video for passed tests
#         try:
#             video_path = page.video.path()
#             if video_path and os.path.exists(video_path):
#                 os.remove(video_path)
#         except Exception as e:
#             print(f"Could not delete video: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Run all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot if test failed
    if report.failed:
        # Get Playwright page fixture if available
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Extends the Pytest report to include screenshots, videos, and traces on failure.
#     """
#     outcome = yield
#     report = outcome.get_result()
#
#     # We only care about the 'call' stage of the test
#     if report.when == "call":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # Test Failed
#             page = item.funcargs.get("page")
#             context = item.funcargs.get("context")
#
#             if page and context:
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 test_name = item.name
#
#                 # 1. Capture Screenshot
#                 screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{test_name}_{timestamp}.png")
#                 page.screenshot(path=screenshot_path)
#                 log.error(f"Test failed: {test_name}. Screenshot saved to {screenshot_path}")
#
#                 # 2. Save Trace
#                 trace_path = os.path.join(TRACES_DIR, f"{test_name}_{timestamp}.zip")
#                 context.tracing.stop(path=trace_path)
#                 log.info(f"Trace saved to {trace_path}")
#             elif page:
#                 # Capture screenshot even if context is missing
#                 timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#                 test_name = item.name
#                 screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{test_name}_{timestamp}.png")
#                 page.screenshot(path=screenshot_path)
#                 log.error(
#                     f"Test failed: {test_name}. Screenshot saved to {screenshot_path} (Context trace not available)")
#
#             # If video was recorded, it's already in VIDEOS_DIR.
#             # We might want to rename it or link it.
#         else:
#             # Test Passed - cleanup artifacts if not wanted
#             context = item.funcargs.get("context")
#             if context:
#                 # Stop tracing without saving
#                 context.tracing.stop()
#
#                 # If it passed and we only want failed videos, we should delete the video
#                 if item.config.getoption("--record-video") == "failed":
#                     page_obj = item.funcargs.get("page")
#                     if page_obj and hasattr(page_obj, "video"):
#                         video = page_obj.video
#                         if video:
#                             video_path = video.path()
#                             # We can't delete it immediately as it's still being written
#                             pass

@pytest.fixture(autouse=True)
def log_test_status(request):
    log.info(f"Starting test: {request.node.name}")
    yield
    log.info(f"Finished test: {request.node.name}")


# Custom marker for blocked tests
def pytest_configure(config):
    config.addinivalue_line("markers", "blocked: mark test as blocked by a bug or environmental issue")
    # Initialize logging
    CustomLogger.setup_logging()
    log.info("Logging system initialized.")


# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([
#         """
#         <h2>QA Dashboard</h2>
#
#         <div style="display:flex;gap:40px;flex-wrap:wrap;">
#             <div>
#                 <h3>Test Result Distribution</h3>
#                 <canvas id="resultChart" width="350"></canvas>
#             </div>
#
#             <div>
#                 <h3>Test Duration</h3>
#                 <canvas id="durationChart" width="500"></canvas>
#             </div>
#         </div>
#
#         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
#
#         <script>
#
#         document.addEventListener("DOMContentLoaded", function(){
#
#             const passed = parseInt(document.querySelector('.passed').innerText);
#             const failed = parseInt(document.querySelector('.failed').innerText);
#             const skipped = parseInt(document.querySelector('.skipped').innerText);
#
#             // PIE CHART
#             new Chart(document.getElementById("resultChart"), {
#                 type: 'pie',
#                 data: {
#                     labels: ["Passed","Failed","Skipped"],
#                     datasets: [{
#                         data: [passed, failed, skipped],
#                         backgroundColor: ["#28a745","#dc3545","#ffc107"]
#                     }]
#                 }
#             });
#
#             // COLLECT TEST DURATIONS
#             const rows = document.querySelectorAll("#results-table tbody");
#             let labels = [];
#             let durations = [];
#
#             rows.forEach(row => {
#                 const cols = row.querySelectorAll("td");
#                 if(cols.length > 2){
#                     labels.push(cols[1].innerText.substring(0,30));
#                     durations.push(parseFloat(cols[2].innerText));
#                 }
#             });
#
#             // BAR CHART
#             new Chart(document.getElementById("durationChart"), {
#                 type: 'bar',
#                 data: {
#                     labels: labels,
#                     datasets: [{
#                         label: "Duration (ms)",
#                         data: durations,
#                         backgroundColor: "#4caf50"
#                     }]
#                 },
#                 options:{
#                     responsive:true,
#                     plugins:{legend:{display:false}},
#                     scales:{
#                         x:{ticks:{display:false}}
#                     }
#                 }
#             });
#
#         });
#
#         </script>
#         """
#     ])