// # backend api
const API_BASE = "http://127.0.0.1:8000";

// ======================================
// DOM ELEMENTS
// ======================================
const form = document.getElementById("predictionForm");
const resultSection = document.getElementById("result");
const predictBtn = document.getElementById("predictBtn");

let customerChart = null;
let metricChart = null;

// ======================================
// FORM SUBMIT
// ======================================

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    predictBtn.disabled = true;
    predictBtn.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    try {

        // Collect form values

        const data = {

            BALANCE: parseFloat(document.getElementById("BALANCE").value),
            BALANCE_FREQUENCY: parseFloat(document.getElementById("BALANCE_FREQUENCY").value),
            PURCHASES: parseFloat(document.getElementById("PURCHASES").value),
            ONEOFF_PURCHASES: parseFloat(document.getElementById("ONEOFF_PURCHASES").value),
            INSTALLMENTS_PURCHASES: parseFloat(document.getElementById("INSTALLMENTS_PURCHASES").value),
            CASH_ADVANCE: parseFloat(document.getElementById("CASH_ADVANCE").value),
            PURCHASES_FREQUENCY: parseFloat(document.getElementById("PURCHASES_FREQUENCY").value),
            CASH_ADVANCE_FREQUENCY: parseFloat(document.getElementById("CASH_ADVANCE_FREQUENCY").value),
            CASH_ADVANCE_TRX: parseInt(document.getElementById("CASH_ADVANCE_TRX").value),
            PURCHASES_TRX: parseInt(document.getElementById("PURCHASES_TRX").value),
            CREDIT_LIMIT: parseFloat(document.getElementById("CREDIT_LIMIT").value),
            PAYMENTS: parseFloat(document.getElementById("PAYMENTS").value),
            MINIMUM_PAYMENTS: parseFloat(document.getElementById("MINIMUM_PAYMENTS").value),
            PRC_FULL_PAYMENT: parseFloat(document.getElementById("PRC_FULL_PAYMENT").value),
            ONEOFF_PURCHASES_FREQUENCY: parseFloat(document.getElementById("ONEOFF_PURCHASES_FREQUENCY").value),
            PURCHASES_INSTALLMENTS_FREQUENCY: parseFloat(document.getElementById("PURCHASES_INSTALLMENTS_FREQUENCY").value),
            TENURE: parseInt(document.getElementById("TENURE").value)

        };

        // Send to FastAPI

        const response = await fetch(`${API_BASE}/predict`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (!response.ok || !result.success) {

            throw new Error(result.detail || "Prediction failed.");

        }

        showResult(result);

    }

    catch (error) {

        alert(error.message);

        console.error(error);

    }

    finally {

        predictBtn.disabled = false;

        predictBtn.innerHTML =
            '<i class="fa-solid fa-wand-magic-sparkles"></i> Predict Customer Segment';

    }

});

// ======================================
// SHOW RESULT
// ======================================

function showResult(result) {

    resultSection.classList.remove("hidden");

    // Segment

    document.getElementById("segmentName").textContent =
        result.segment;

    document.getElementById("segmentDescription").textContent =
        result.description;

    document.getElementById("summaryCluster").textContent =
        result.cluster;

    document.getElementById("summaryStatus").textContent =
        "Completed";
    // ===========================
    // Update KPI Cards
    // ===========================

    document.getElementById("kpiSegment").textContent =
        result.segment;

    document.getElementById("kpiCluster").textContent =
        result.cluster;

    document.getElementById("kpiUtilization").textContent =
        (result.metrics["Credit Utilization"] * 100).toFixed(1) + "%";

    document.getElementById("kpiStatus").textContent =
        "Completed";

    // Metrics

    updateMetrics(result.metrics);

    // Recommendations

    updateRecommendations(result.recommendation);

    // Charts

    createCharts(result.metrics);

    // Scroll to results

    resultSection.scrollIntoView({
        behavior: "smooth"
    });

}

// ======================================
// UPDATE METRICS
// ======================================

function updateMetrics(metrics) {

    const utilization = Math.min(
        metrics["Credit Utilization"] * 100,
        100
    );

    const payment = Math.min(
        metrics["Payment Ratio"] * 100,
        100
    );

    document.getElementById("utilizationBar").style.width =
        utilization + "%";

    document.getElementById("paymentBar").style.width =
        payment + "%";

    animateValue(
    "utilizationValue",
    utilization,
    "",
    "%"
    );

    animateValue(
        "paymentValue",
        payment,
        "",
        "%"
    );

    animateValue(
        "remainingCredit",
        metrics["Remaining Credit"],
        "$"
    );

    animateValue(
        "averagePurchase",
        metrics["Average Purchase"],
        "$"
    );

}

// ======================================
// RECOMMENDATIONS
// ======================================

function updateRecommendations(items) {

    const list =
        document.getElementById("recommendations");

    list.innerHTML = "";

    items.forEach(item => {

        const li = document.createElement("li");

        li.innerHTML =
            `<i class="fa-solid fa-check-circle"></i> ${item}`;

        list.appendChild(li);

    });

}

function animateValue(id, endValue, prefix = "", suffix = "") {

    const element = document.getElementById(id);

    const duration = 800;

    const start = 0;

    const stepTime = 15;

    const increment = endValue / (duration / stepTime);

    let current = start;

    const timer = setInterval(() => {

        current += increment;

        if(current >= endValue){

            current = endValue;

            clearInterval(timer);

        }

        element.textContent =
            prefix +
            current.toFixed(1) +
            suffix;

    }, stepTime);

}

// ======================================
// CHARTS
// ======================================

function createCharts(metrics) {

    // Destroy old charts

    if (customerChart)
        customerChart.destroy();

    if (metricChart)
        metricChart.destroy();

    // Customer Profile

    customerChart = new Chart(

        document.getElementById("customerChart"),

        {

            type: "doughnut",

            data: {

                labels: [

                    "Used Credit",

                    "Remaining Credit"

                ],

                datasets: [{

                    data: [

                        metrics["Credit Utilization"] * 100,

                        100 - (metrics["Credit Utilization"] * 100)

                    ]

                }]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );

    // Financial Metrics

    metricChart = new Chart(

        document.getElementById("metricChart"),

        {

            type: "bar",

            data: {

                labels: [

                    "Payment",

                    "Purchase",

                    "Remaining"

                ],

                datasets: [{

                    label: "Customer",

                    data: [

                        metrics["Payment Ratio"],

                        metrics["Average Purchase"],

                        metrics["Remaining Credit"]

                    ]

                }]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        }

    );

}