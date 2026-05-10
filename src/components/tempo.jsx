import React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';

const Tempo = () => {
    const desktopOS = [
        { id: 0, value: 40, label: 'Windows', color: '#1976d2' },
        { id: 1, value: 30, label: 'macOS', color: '#9c27b0' },
        { id: 2, value: 20, label: 'Linux', color: '#4caf50' },
        { id: 3, value: 10, label: 'Other', color: '#ff9800' },
    ];

    const valueFormatter = (value) => `${value}%`;

    return (
        <>
            <div>Tempo</div>
            <PieChart
                series={[
                    {
                        data: desktopOS,
                        highlightScope: { fade: 'global', highlight: 'item' },
                        faded: { innerRadius: 30, additionalRadius: -30, color: 'gray' },
                        valueFormatter,
                    },
                ]}
                height={200}
                width={400}
            />

        </>
    );
};

export default Tempo;
