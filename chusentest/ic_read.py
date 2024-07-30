from smartcard.util import toHexString
from smartcard.System import readers as get_readers
readers = get_readers()
print(readers)

conn = readers[0].createConnection()
conn.connect()

send_data = [0xFF, 0xCA, 0x00, 0x00, 0x00]
recv_data, sw1, sw2 = conn.transmit(send_data)
print(toHexString(send_data))
