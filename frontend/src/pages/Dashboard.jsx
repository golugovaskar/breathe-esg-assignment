import { useEffect, useRef, useState } from "react";
import api from "../services/api";

function Dashboard() {
    const [stats, setStats] = useState(null);
    const [records, setRecords] = useState([]);
    const [filter, setFilter] = useState("ALL");

    const sapRef = useRef(null);
    const utilityRef = useRef(null);
    const travelRef = useRef(null);

    useEffect(() => {
        fetchStats();
        fetchRecords();
    }, []);

    const fetchStats = async () => {
        try {
            const res = await api.get("/dashboard/stats/");
            setStats(res.data);
        } catch (error) {
            console.log(error);
        }
    };

    const fetchRecords = async () => {
        try {
            const res = await api.get("/emissions/records/");
            setRecords(res.data);
        } catch (error) {
            console.log(error);
        }
    };

    const reviewRecord = async (id, action) => {
        try {
            await api.post(`/review/${id}/`, {
                action,
                comment: `${action} from dashboard`,
            });

            fetchStats();
            fetchRecords();
        } catch (error) {
            console.log(error);
        }
    };

    const uploadFile = async (file, endpoint) => {
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            await api.post(endpoint, formData);

            alert("Upload successful ✅");

            fetchStats();
            fetchRecords();
        } catch (error) {
            console.log(error);
            alert("Upload failed ❌");
        }
    };


    const filteredRecords = records.filter((record) => {
    if (filter === "ALL") return true;

    if (filter === "SUSPICIOUS") {
        return record.suspicious;
    }

    return record.status === filter;
    });
    const getStatusStyle = (status) => {
        switch (status) {
            case "APPROVED":
                return {
                    background: "#dcfce7",
                    color: "#166534",
                };

            case "REJECTED":
                return {
                    background: "#fee2e2",
                    color: "#991b1b",
                };

            default:
                return {
                    background: "#fef3c7",
                    color: "#92400e",
                };
        }
    };

    return (
        <div
            style={{
                background: "#f4f6fb",
                minHeight: "100vh",
                padding: "40px",
            }}
        >
            <div style={{ marginBottom: "30px" }}>
                <h1
                    style={{
                        fontSize: "42px",
                        color: "#1e293b",
                    }}
                >
                    ESG Dashboard
                </h1>

                <p
                    style={{
                        color: "#64748b",
                        fontSize: "18px",
                    }}
                >
                    Sustainability Data Monitoring Platform
                </p>
            </div>

            {!stats ? (
                <h2>Loading...</h2>
            ) : (
                <>
                    <div
                        style={{
                            display: "grid",
                            gridTemplateColumns: "repeat(4,1fr)",
                            gap: "24px",
                        }}
                    >
                        <Card title="Total Records" value={stats.total_records} />
                        <Card title="Approved" value={stats.approved_records} />
                        <Card title="Pending" value={stats.pending_records} />
                        <Card title="Suspicious" value={stats.suspicious_records} />
                        <Card title="Scope 1" value={stats.scope_1_count} />
                        <Card title="Scope 2" value={stats.scope_2_count} />
                        <Card title="Scope 3" value={stats.scope_3_count} />
                    </div>

                    <div style={sectionStyle}>
                        <h2
                            style={{
                                color: "#0f172a",
                                fontSize: "30px",
                                marginBottom: "24px",
                            }}
                        >
                            Upload ESG Files
                        </h2>

                        <div style={{ display: "flex", gap: "16px" }}>
                            <button
                                style={buttonStyle}
                                onClick={() => sapRef.current.click()}
                            >
                                Upload SAP CSV
                            </button>

                            <button
                                style={buttonStyle}
                                onClick={() => utilityRef.current.click()}
                            >
                                Upload Utility CSV
                            </button>

                            <button
                                style={buttonStyle}
                                onClick={() => travelRef.current.click()}
                            >
                                Upload Travel CSV
                            </button>
                        </div>

                        <input
                            hidden
                            type="file"
                            ref={sapRef}
                            onChange={(e) =>
                                uploadFile(e.target.files[0], "/sap-upload/")
                            }
                        />

                        <input
                            hidden
                            type="file"
                            ref={utilityRef}
                            onChange={(e) =>
                                uploadFile(
                                    e.target.files[0],
                                    "/utility-upload/"
                                )
                            }
                        />

                        <input
                            hidden
                            type="file"
                            ref={travelRef}
                            onChange={(e) =>
                                uploadFile(
                                    e.target.files[0],
                                    "/travel-upload/"
                                )
                            }
                        />
                    </div>

                    <div style={sectionStyle}>
                        <h2
                            style={{
                                color: "#0f172a",
                                fontSize: "30px",
                                marginBottom: "10px",
                            }}
                        >
                            Emission Records
                        </h2>


                        <div
    style={{
        display: "flex",
        gap: "12px",
        marginTop: "20px",
        marginBottom: "25px",
        flexWrap: "wrap",
    }}
>
    <button
        style={getFilterButtonStyle(filter === "ALL")}
        onClick={() => setFilter("ALL")}
    >
        All
    </button>

    <button
        style={getFilterButtonStyle(filter === "PENDING")}
        onClick={() => setFilter("PENDING")}
    >
        Pending
    </button>

    <button
        style={getFilterButtonStyle(filter === "APPROVED")}
        onClick={() => setFilter("APPROVED")}
    >
        Approved
    </button>

    <button
        style={getFilterButtonStyle(filter === "REJECTED")}
        onClick={() => setFilter("REJECTED")}
    >
        Rejected
    </button>

    <button
        style={getFilterButtonStyle(filter === "SUSPICIOUS")}
        onClick={() => setFilter("SUSPICIOUS")}
    >
        Suspicious
    </button>
</div>

                        <table
                            style={{
                                width: "100%",
                                borderCollapse: "collapse",
                                marginTop: "25px",
                            }}
                        >
                            <thead>
                                <tr style={{ textAlign: "left" }}>
                                    <th style={thStyle}>Activity</th>
                                    <th style={thStyle}>Scope</th>
                                    <th style={thStyle}>Status</th>
                                    <th style={thStyle}>Suspicious</th>
                                    <th style={thStyle}>Actions</th>
                                </tr>
                            </thead>

                            <tbody>
                                {filteredRecords.map((record) => (
                                    <tr
                                        key={record.id}
                                        style={{
                                            borderBottom: "1px solid #eee",
                                        }}
                                    >
                                        <td style={tdStyle}>
                                            {record.activity_type}
                                        </td>

                                        <td style={tdStyle}>
                                            {record.scope}
                                        </td>

                                        <td style={tdStyle}>
                                            <span
                                                style={{
                                                    padding: "8px 14px",
                                                    borderRadius: "999px",
                                                    fontWeight: "600",
                                                    ...getStatusStyle(record.status),
                                                }}
                                            >
                                                {record.status}
                                            </span>
                                        </td>

                                        <td style={tdStyle}>
                                            {record.suspicious ? (
                                                <span style={warningBadge}>
                                                    ⚠ Suspicious
                                                </span>
                                            ) : (
                                                <span style={safeBadge}>
                                                    ✓ Safe
                                                </span>
                                            )}
                                        </td>

                                        <td style={tdStyle}>
                                            <button
                                                style={approveBtn}
                                                onClick={() =>
                                                    reviewRecord(
                                                        record.id,
                                                        "APPROVED"
                                                    )
                                                }
                                            >
                                                Approve
                                            </button>

                                            <button
                                                style={rejectBtn}
                                                onClick={() =>
                                                    reviewRecord(
                                                        record.id,
                                                        "REJECTED"
                                                    )
                                                }
                                            >
                                                Reject
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </>
            )}
        </div>
    );
}

function Card({ title, value }) {
    return (
        <div
            style={{
                background: "white",
                padding: "28px",
                borderRadius: "22px",
                boxShadow: "0 8px 20px rgba(0,0,0,0.08)",
            }}
        >
            <h3 style={{ color: "#64748b" }}>{title}</h3>

            <h1
                style={{
                    fontSize: "42px",
                    color: "#0f172a",
                }}
            >
                {value}
            </h1>
        </div>
    );
}

const sectionStyle = {
    background: "white",
    marginTop: "40px",
    padding: "35px",
    borderRadius: "24px",
    boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
};

const thStyle = {
    padding: "20px",
    color: "#334155",
    fontSize: "17px",
    fontWeight: "700",
    borderBottom: "2px solid #e2e8f0",
};


const tdStyle = {
    padding: "24px 20px",
    color: "#1e293b",
    fontSize: "16px",
};


const warningBadge = {
    background: "#fef3c7",
    color: "#92400e",
    padding: "8px 12px",
    borderRadius: "999px",
};

const safeBadge = {
    background: "#dcfce7",
    color: "#166534",
    padding: "8px 12px",
    borderRadius: "999px",
};

const buttonStyle = {
    background: "#2563eb",
    color: "white",
    border: "none",
    padding: "14px 22px",
    borderRadius: "12px",
    cursor: "pointer",
    fontWeight: "600",
};

const approveBtn = {
    background: "#16a34a",
    color: "white",
    border: "none",
    padding: "10px 16px",
    borderRadius: "10px",
    marginRight: "10px",
    cursor: "pointer",
};

const rejectBtn = {
    background: "#dc2626",
    color: "white",
    border: "none",
    padding: "10px 16px",
    borderRadius: "10px",
    cursor: "pointer",
};


const getFilterButtonStyle = (active) => ({
    background: active ? "#2563eb" : "#e2e8f0",
    color: active ? "white" : "#1e293b",
    border: "none",
    padding: "10px 18px",
    borderRadius: "12px",
    cursor: "pointer",
    fontWeight: "600",
});

export default Dashboard;