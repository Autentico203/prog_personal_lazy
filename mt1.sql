SELECT AVG(annualSalary) AS avgsalary, grade, COUNT(empId) AS employeeCount
FROM Salary_Grade S JOIN (SELECT empID, annualSalary
													FROM Department NATURAL JOIN Employee 
													WHERE jobTitle='manager' AND empName NOT LIKE 'C%' AND (deptLocation = 'Pairs' OR deptLocation = 'Tokyo' OR deptLocation = 'Brazil') AS T)
													ON (T.annualSalary >= S.minAnnualSalary AND T.annualSalary <= S.maxAnnualSalary)
GROUP BY grade 
HAVING COUNT(empID) <= 4
ORDER BY grade